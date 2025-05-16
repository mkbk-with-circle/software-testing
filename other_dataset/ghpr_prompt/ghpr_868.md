## Buggy code
```java
package org.apereo.cas.util.cipher;

import lombok.SneakyThrows;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.lang3.StringUtils;
import org.apereo.cas.util.EncodingUtils;
import org.apereo.cas.util.gen.Base64RandomStringGenerator;
import org.jose4j.jwk.JsonWebKey;
import org.jose4j.jwk.OctJwkGenerator;
import org.jose4j.jwk.OctetSequenceJsonWebKey;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.Map;

import lombok.Getter;
import lombok.Setter;

/**
 * This is {@link BaseBinaryCipherExecutor}.
 * <p>
 * A implementation that is based on algorithms
 * provided by the default platform's JCE. By default AES encryption is
 * used.
 *
 * @author Misagh Moayyed
 * @since 4.2
 */
@Slf4j
@Getter
@Setter
public abstract class BaseBinaryCipherExecutor extends AbstractCipherExecutor<byte[], byte[]> {

    /**
     * Name of the cipher/component whose keys are generated here.
     */
    protected final String cipherName;

    /**
     * Secret key IV algorithm. Default is {@code AES}.
     */
    private String secretKeyAlgorithm = "AES";

    private byte[] encryptionSecretKey;

    private final SecretKeySpec encryptionKey;

    private final Cipher aesCipher;

    /**
     * Instantiates a new cryptic ticket cipher executor.
     *
     * @param encryptionSecretKey the encryption secret key, base64 encoded
     * @param signingSecretKey    the signing key
     * @param signingKeySize      the signing key size
     * @param encryptionKeySize   the encryption key size
     * @param cipherName          the cipher name
     */
    @SneakyThrows
    public BaseBinaryCipherExecutor(final String encryptionSecretKey, final String signingSecretKey,
                                    final int signingKeySize, final int encryptionKeySize, final String cipherName) {
        this.cipherName = cipherName;
        ensureSigningKeyExists(signingSecretKey, signingKeySize);
        ensureEncryptionKeyExists(encryptionSecretKey, encryptionKeySize);
        this.encryptionKey = new SecretKeySpec(this.encryptionSecretKey, this.secretKeyAlgorithm);
        this.aesCipher = Cipher.getInstance("AES");
    }

    @Override
    @SneakyThrows
    public byte[] encode(final byte[] value, final Object[] parameters) {
        this.aesCipher.init(Cipher.ENCRYPT_MODE, this.encryptionKey);
        final byte[] result = this.aesCipher.doFinal(value);
        return sign(result);
    }

    @Override
    @SneakyThrows
    public byte[] decode(final byte[] value, final Object[] parameters) {
        final byte[] verifiedValue = verifySignature(value);
        this.aesCipher.init(Cipher.DECRYPT_MODE, this.encryptionKey);
        final byte[] bytePlainText = aesCipher.doFinal(verifiedValue);
        return bytePlainText;
    }

    @SneakyThrows
    private static String generateOctetJsonWebKeyOfSize(final int size) {
        final OctetSequenceJsonWebKey octetKey = OctJwkGenerator.generateJwk(size);
        final Map<String, Object> params = octetKey.toParams(JsonWebKey.OutputControlLevel.INCLUDE_SYMMETRIC);
        return params.get("k").toString();
    }

    /**
     * Gets encryption key setting.
     *
     * @return the encryption key setting
     */
    protected abstract String getEncryptionKeySetting();

    /**
     * Gets signing key setting.
     *
     * @return the signing key setting
     */
    protected abstract String getSigningKeySetting();

    private void ensureEncryptionKeyExists(final String encryptionSecretKey, final int encryptionKeySize) {
        final byte[] encryptionKey;
        if (StringUtils.isBlank(encryptionSecretKey)) {
            LOGGER.warn("Secret key for encryption is not defined under [{}]. CAS will attempt to auto-generate the encryption key",
                getEncryptionKeySetting());
            final String key = new Base64RandomStringGenerator(encryptionKeySize).getNewString();
            LOGGER.warn("Generated encryption key [{}] of size [{}]. The generated key MUST be added to CAS settings under setting [{}].",
                key, encryptionKeySize, getEncryptionKeySetting());
            encryptionKey = EncodingUtils.decodeBase64(key);
        } else {
            final boolean base64 = EncodingUtils.isBase64(encryptionSecretKey);
            byte[] key = new byte[0];
            if (base64) {
                key = EncodingUtils.decodeBase64(encryptionSecretKey);
            }
            if (base64 && key.length == encryptionKeySize) {
                LOGGER.debug("Secret key for encryption defined under [{}] is Base64 encoded.", getEncryptionKeySetting());
                encryptionKey = key;
            } else if (encryptionSecretKey.length() != encryptionKeySize) {
                LOGGER.warn("Secret key for encryption defined under [{}] is Base64 encoded but the size does not match the key size [{}].",
                    getEncryptionKeySetting(), encryptionKeySize);
                encryptionKey = encryptionSecretKey.getBytes(StandardCharsets.UTF_8);
            } else {
                LOGGER.warn("Secret key for encryption defined under [{}] is not Base64 encoded. Clear the setting to regenerate (Recommended) or replace with"
                    + " [{}].", getEncryptionKeySetting(), EncodingUtils.encodeBase64(encryptionSecretKey));
                encryptionKey = encryptionSecretKey.getBytes(StandardCharsets.UTF_8);
            }
        }
        this.encryptionSecretKey = encryptionKey;
    }

    private void ensureSigningKeyExists(final String signingSecretKey, final int signingKeySize) {
        String signingKeyToUse = signingSecretKey;
        if (StringUtils.isBlank(signingKeyToUse)) {
            LOGGER.warn("Secret key for signing is not defined under [{}]. CAS will attempt to auto-generate the signing key",
                getSigningKeySetting());
            signingKeyToUse = generateOctetJsonWebKeyOfSize(signingKeySize);
            LOGGER.warn("Generated signing key [{}] of size [{}]. The generated key MUST be added to CAS settings under setting [{}].",
                signingKeyToUse, signingKeySize, getSigningKeySetting());
        }
        configureSigningKey(signingKeyToUse);
    }
}

```

## Error
[5.3] Fix potential non-threadsafe usage for Cipher class

## Error Description
## Brief description of changes applied

A possible non-threadsafe usage of Cipher is seen `BaseBinaryCipherExecutor.java`. This will make it so that occasionally there will be _Cipher related exception_ when CAS server undergoes high stress. The exception are like these:
```
java.lang.IllegalStateException: Cipher not initialized
javax.crypto.BadPaddingException: Given final block not properly padded. Such issues can arise if a bad key is used during decryption.
javax.crypto.IllegalBlockSizeException: Input length must be multiple of 16 when decrypting with padded cipher
```

Cipher is stateful, as explain in this stackoverflow [post](https://stackoverflow.com/questions/6957406/is-cipher-thread-safe), so the class should be initialized right before it is used, instead of initializing in the constructor of `BaseBinaryCipherExecutor.java`. 

After the changes in this PR, The Cipher exception problem is fixed.

## Any documentation on how to configure, test

   1. Before applying this fix, enabled Hazelcast ticketing with encryption (1 member in the cluster is fine)
   2. Use JMeter to stress test (this [JMeter script](https://github.com/apereo/cas/blob/v5.3.6/etc/loadtests/jmeter/CAS_CAS.jmx) provided inside CAS will work just fine: )
   3. Stress it high enough for < 5 mins (for me, 1 req / second does the trick)
   4. You should be able to see multiple exception like the above exists before this fix
   5. And the exception will be gone after the fix

## Any possible limitations, side effects, etc

The only tested ticket registry is `Hazelcast`. Other ticket registry is not tested, since I do not have the resource to test out those ticket registry methods.

## Reference any other pull requests that might be related.

CAS Community Google Group discussion related to this issue:
https://groups.google.com/a/apereo.org/forum/#!topic/cas-user/htBkshVVaFg


<!--

# Contributing

First off, thank you for considering to contribute to CAS. 

# Details

Closes #IssueNumber

Ensure that you include the following:

- [] Brief description of changes applied
- [] Any documentation on how to configure, test
- [] Any possible limitations, side effects, etc
- [] Reference any other pull requests that might be related.

-->

