## Lang_1
Lang_1: Running ant (compile.tests)................................................ FAIL
Executed command:  cd /ymy/test/Lang_1_buggy && /opt/defects4j/major/bin/ant -f /opt/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/opt/defects4j -Dd4j.dir.projects=/opt/defects4j/framework/projects -Dbasedir=/ymy/test/Lang_1_buggy  compile.tests 2>&1
Buildfile: /opt/defects4j/framework/projects/defects4j.build.xml

init:
     [echo] -------- commons-lang3 3.2-SNAPSHOT --------

compile:
    [javac] Compiling 1 source file to /ymy/test/Lang_1_buggy/target/classes
    [javac] warning: [options] bootstrap class path not set in conjunction with -source 6
    [javac] warning: [options] source value 6 is obsolete and will be removed in a future release
    [javac] warning: [options] target value 1.6 is obsolete and will be removed in a future release
    [javac] warning: [options] To suppress warnings about obsolete options, use -Xlint:-options.
    [javac] /ymy/test/Lang_1_buggy/src/main/java/org/apache/commons/lang3/math/NumberUtils.java:492: error: ')' expected
    [javac]                     && (numeric.charAt(0) == '-' && isDigits(numeric.substring(1)) || isDigits(numeric)) {
    [javac]                                                                                                         ^
    [javac] 1 error
    [javac] 4 warnings

BUILD FAILED
/ymy/test/Lang_1_buggy/build.xml:63: Compile failed; see the compiler error output for details.

Total time: 0 seconds
Cannot compile test suite! at /opt/defects4j/framework/bin/d4j/d4j-test line 134.
Compilation failed in require at /opt/defects4j/framework/bin/defects4j line 195.

## Lang_1
Lang_1: Running ant (compile.tests)................................................ FAIL
Executed command:  cd /ymy/test/Lang_1_buggy && /opt/defects4j/major/bin/ant -f /opt/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/opt/defects4j -Dd4j.dir.projects=/opt/defects4j/framework/projects -Dbasedir=/ymy/test/Lang_1_buggy  compile.tests 2>&1
Buildfile: /opt/defects4j/framework/projects/defects4j.build.xml

init:
     [echo] -------- commons-lang3 3.2-SNAPSHOT --------
    [mkdir] Created dir: /ymy/test/Lang_1_buggy/target

compile:
    [mkdir] Created dir: /ymy/test/Lang_1_buggy/target/classes
    [javac] Compiling 108 source files to /ymy/test/Lang_1_buggy/target/classes
    [javac] warning: [options] bootstrap class path not set in conjunction with -source 6
    [javac] warning: [options] source value 6 is obsolete and will be removed in a future release
    [javac] warning: [options] target value 1.6 is obsolete and will be removed in a future release
    [javac] warning: [options] To suppress warnings about obsolete options, use -Xlint:-options.
    [javac] /ymy/test/Lang_1_buggy/src/main/java/org/apache/commons/lang3/math/NumberUtils.java:492: error: ')' expected
    [javac]                     && (numeric.charAt(0) == '-' && isDigits(numeric.substring(1)) || isDigits(numeric)) {
    [javac]                                                                                                         ^
    [javac] 1 error
    [javac] 4 warnings

BUILD FAILED
/ymy/test/Lang_1_buggy/build.xml:63: Compile failed; see the compiler error output for details.

Total time: 1 second
Cannot compile test suite! at /opt/defects4j/framework/bin/d4j/d4j-test line 134.
Compilation failed in require at /opt/defects4j/framework/bin/defects4j line 195.

## Lang_3
Lang_3: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 0

## Lang_4
Lang_4: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang3.text.translate.LookupTranslatorTest::testLang882

## Lang_5
Lang_5: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 0

## Lang_6
Lang_6: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 2
  - org.apache.commons.lang3.StringEscapeUtilsTest::testEscapeXmlSupplementaryCharacters
  - org.apache.commons.lang3.text.translate.NumericEntityEscaperTest::testSupplementary

## Lang_7
Lang_7: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 0

## Lang_8
Lang_8: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 2
  - org.apache.commons.lang3.time.FastDateFormat_PrinterTest::testCalendarTimezoneRespected
  - org.apache.commons.lang3.time.FastDatePrinterTest::testCalendarTimezoneRespected

## Lang_9
Lang_9: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 2
  - org.apache.commons.lang3.time.FastDateFormat_ParserTest::testLANG_832
  - org.apache.commons.lang3.time.FastDateParserTest::testLANG_832

## Lang_10
Lang_10: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 2
  - org.apache.commons.lang3.time.FastDateFormat_ParserTest::testLANG_831
  - org.apache.commons.lang3.time.FastDateParserTest::testLANG_831

## Lang_11
Lang_11: Running ant (compile.tests)................................................ FAIL
Executed command:  cd /ymy/test/Lang_11_buggy && /opt/defects4j/major/bin/ant -f /opt/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/opt/defects4j -Dd4j.dir.projects=/opt/defects4j/framework/projects -Dbasedir=/ymy/test/Lang_11_buggy  compile.tests 2>&1
Buildfile: /opt/defects4j/framework/projects/defects4j.build.xml

init:
     [echo] -------- commons-lang3 3.2-SNAPSHOT --------
    [mkdir] Created dir: /ymy/test/Lang_11_buggy/target

compile:
    [mkdir] Created dir: /ymy/test/Lang_11_buggy/target/classes
    [javac] Compiling 106 source files to /ymy/test/Lang_11_buggy/target/classes
    [javac] warning: [options] bootstrap class path not set in conjunction with -source 6
    [javac] warning: [options] source value 6 is obsolete and will be removed in a future release
    [javac] warning: [options] target value 1.6 is obsolete and will be removed in a future release
    [javac] warning: [options] To suppress warnings about obsolete options, use -Xlint:-options.
    [javac] /ymy/test/Lang_11_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:235: error: <identifier> expected
    [javac]                         count--;
    [javac]                              ^
    [javac] /ymy/test/Lang_11_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:236: error: ']' expected
    [javac]                         buffer[count] = (char) (55296 + random.nextInt(128));
    [javac]                                ^
    [javac] /ymy/test/Lang_11_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:236: error: ';' expected
    [javac]                         buffer[count] = (char) (55296 + random.nextInt(128));
    [javac]                                     ^
    [javac] /ymy/test/Lang_11_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:236: error: <identifier> expected
    [javac]                         buffer[count] = (char) (55296 + random.nextInt(128));
    [javac]                                              ^
    [javac] /ymy/test/Lang_11_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:236: error: <identifier> expected
    [javac]                         buffer[count] = (char) (55296 + random.nextInt(128));
    [javac]                                                                       ^
    [javac] /ymy/test/Lang_11_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:236: error: illegal start of type
    [javac]                         buffer[count] = (char) (55296 + random.nextInt(128));
    [javac]                                                                        ^
    [javac] /ymy/test/Lang_11_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:238: error: class, interface, or enum expected
    [javac]                 } else if(ch >= 55296 && ch <= 56191) {
    [javac]                 ^
    [javac] /ymy/test/Lang_11_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:241: error: class, interface, or enum expected
    [javac]                     } else {
    [javac]                     ^
    [javac] /ymy/test/Lang_11_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:244: error: class, interface, or enum expected
    [javac]                         count--;
    [javac]                         ^
    [javac] /ymy/test/Lang_11_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:245: error: class, interface, or enum expected
    [javac]                         buffer[count] = ch;
    [javac]                         ^
    [javac] /ymy/test/Lang_11_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:246: error: class, interface, or enum expected
    [javac]                     }
    [javac]                     ^
    [javac] /ymy/test/Lang_11_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:250: error: class, interface, or enum expected
    [javac]                 } else {
    [javac]                 ^
    [javac] /ymy/test/Lang_11_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:252: error: class, interface, or enum expected
    [javac]                 }
    [javac]                 ^
    [javac] /ymy/test/Lang_11_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:255: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_11_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:258: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_11_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:274: error: class, interface, or enum expected
    [javac]     public static String random(int count, String chars) {
    [javac]                   ^
    [javac] /ymy/test/Lang_11_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:277: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_11_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:279: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_11_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:293: error: class, interface, or enum expected
    [javac]     public static String random(int count, char... chars) {
    [javac]                   ^
    [javac] /ymy/test/Lang_11_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:296: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_11_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:298: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] 21 errors
    [javac] 4 warnings

BUILD FAILED
/ymy/test/Lang_11_buggy/build.xml:63: Compile failed; see the compiler error output for details.

Total time: 0 seconds
Cannot compile test suite! at /opt/defects4j/framework/bin/d4j/d4j-test line 134.
Compilation failed in require at /opt/defects4j/framework/bin/defects4j line 195.

## Lang_12
Lang_12: Running ant (compile.tests)................................................ FAIL
Executed command:  cd /ymy/test/Lang_12_buggy && /opt/defects4j/major/bin/ant -f /opt/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/opt/defects4j -Dd4j.dir.projects=/opt/defects4j/framework/projects -Dbasedir=/ymy/test/Lang_12_buggy  compile.tests 2>&1
Buildfile: /opt/defects4j/framework/projects/defects4j.build.xml

init:
     [echo] -------- commons-lang3 3.2-SNAPSHOT --------
    [mkdir] Created dir: /ymy/test/Lang_12_buggy/target

compile:
    [mkdir] Created dir: /ymy/test/Lang_12_buggy/target/classes
    [javac] Compiling 106 source files to /ymy/test/Lang_12_buggy/target/classes
    [javac] warning: [options] bootstrap class path not set in conjunction with -source 6
    [javac] warning: [options] source value 6 is obsolete and will be removed in a future release
    [javac] warning: [options] target value 1.6 is obsolete and will be removed in a future release
    [javac] warning: [options] To suppress warnings about obsolete options, use -Xlint:-options.
    [javac] /ymy/test/Lang_12_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:229: error: <identifier> expected
    [javac]                         count--;
    [javac]                              ^
    [javac] /ymy/test/Lang_12_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:230: error: ']' expected
    [javac]                         buffer[count] = (char) (55296 + random.nextInt(128));
    [javac]                                ^
    [javac] /ymy/test/Lang_12_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:230: error: ';' expected
    [javac]                         buffer[count] = (char) (55296 + random.nextInt(128));
    [javac]                                     ^
    [javac] /ymy/test/Lang_12_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:230: error: <identifier> expected
    [javac]                         buffer[count] = (char) (55296 + random.nextInt(128));
    [javac]                                              ^
    [javac] /ymy/test/Lang_12_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:230: error: <identifier> expected
    [javac]                         buffer[count] = (char) (55296 + random.nextInt(128));
    [javac]                                                                       ^
    [javac] /ymy/test/Lang_12_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:230: error: illegal start of type
    [javac]                         buffer[count] = (char) (55296 + random.nextInt(128));
    [javac]                                                                        ^
    [javac] /ymy/test/Lang_12_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:232: error: class, interface, or enum expected
    [javac]                 } else if(ch >= 55296 && ch <= 56191) {
    [javac]                 ^
    [javac] /ymy/test/Lang_12_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:235: error: class, interface, or enum expected
    [javac]                     } else {
    [javac]                     ^
    [javac] /ymy/test/Lang_12_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:238: error: class, interface, or enum expected
    [javac]                         count--;
    [javac]                         ^
    [javac] /ymy/test/Lang_12_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:239: error: class, interface, or enum expected
    [javac]                         buffer[count] = ch;
    [javac]                         ^
    [javac] /ymy/test/Lang_12_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:240: error: class, interface, or enum expected
    [javac]                     }
    [javac]                     ^
    [javac] /ymy/test/Lang_12_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:244: error: class, interface, or enum expected
    [javac]                 } else {
    [javac]                 ^
    [javac] /ymy/test/Lang_12_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:246: error: class, interface, or enum expected
    [javac]                 }
    [javac]                 ^
    [javac] /ymy/test/Lang_12_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:249: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_12_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:252: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_12_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:268: error: class, interface, or enum expected
    [javac]     public static String random(int count, String chars) {
    [javac]                   ^
    [javac] /ymy/test/Lang_12_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:271: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_12_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:273: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_12_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:287: error: class, interface, or enum expected
    [javac]     public static String random(int count, char... chars) {
    [javac]                   ^
    [javac] /ymy/test/Lang_12_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:290: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_12_buggy/src/main/java/org/apache/commons/lang3/RandomStringUtils.java:292: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] 21 errors
    [javac] 4 warnings

BUILD FAILED
/ymy/test/Lang_12_buggy/build.xml:63: Compile failed; see the compiler error output for details.

Total time: 0 seconds
Cannot compile test suite! at /opt/defects4j/framework/bin/d4j/d4j-test line 134.
Compilation failed in require at /opt/defects4j/framework/bin/defects4j line 195.

## Lang_13
Lang_13: Running ant (compile.tests)................................................ FAIL
Executed command:  cd /ymy/test/Lang_13_buggy && /opt/defects4j/major/bin/ant -f /opt/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/opt/defects4j -Dd4j.dir.projects=/opt/defects4j/framework/projects -Dbasedir=/ymy/test/Lang_13_buggy  compile.tests 2>&1
Buildfile: /opt/defects4j/framework/projects/defects4j.build.xml

init:
     [echo] -------- commons-lang3 3.2-SNAPSHOT --------
    [mkdir] Created dir: /ymy/test/Lang_13_buggy/target

compile:
    [mkdir] Created dir: /ymy/test/Lang_13_buggy/target/classes
    [javac] Compiling 106 source files to /ymy/test/Lang_13_buggy/target/classes
    [javac] warning: [options] bootstrap class path not set in conjunction with -source 6
    [javac] warning: [options] source value 6 is obsolete and will be removed in a future release
    [javac] warning: [options] target value 1.6 is obsolete and will be removed in a future release
    [javac] warning: [options] To suppress warnings about obsolete options, use -Xlint:-options.
    [javac] /ymy/test/Lang_13_buggy/src/main/java/org/apache/commons/lang3/SerializationUtils.java:225: error: multi-catch statements are not supported in -source 6
    [javac]         } catch (ClassNotFoundException | IOException ex) {
    [javac]                                         ^
    [javac]   (use -source 7 or higher to enable multi-catch statements)
    [javac] 1 error
    [javac] 4 warnings

BUILD FAILED
/ymy/test/Lang_13_buggy/build.xml:63: Compile failed; see the compiler error output for details.

Total time: 0 seconds
Cannot compile test suite! at /opt/defects4j/framework/bin/d4j/d4j-test line 134.
Compilation failed in require at /opt/defects4j/framework/bin/defects4j line 195.

## Lang_14
Lang_14: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 0

## Lang_15
Lang_15: Running ant (compile.tests)................................................ FAIL
Executed command:  cd /ymy/test/Lang_15_buggy && /opt/defects4j/major/bin/ant -f /opt/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/opt/defects4j -Dd4j.dir.projects=/opt/defects4j/framework/projects -Dbasedir=/ymy/test/Lang_15_buggy  compile.tests 2>&1
Buildfile: /opt/defects4j/framework/projects/defects4j.build.xml

init:
     [echo] -------- commons-lang3 3.2-SNAPSHOT --------
    [mkdir] Created dir: /ymy/test/Lang_15_buggy/target

compile:
    [mkdir] Created dir: /ymy/test/Lang_15_buggy/target/classes
    [javac] Compiling 99 source files to /ymy/test/Lang_15_buggy/target/classes
    [javac] warning: [options] bootstrap class path not set in conjunction with -source 6
    [javac] warning: [options] source value 6 is obsolete and will be removed in a future release
    [javac] warning: [options] target value 1.6 is obsolete and will be removed in a future release
    [javac] warning: [options] To suppress warnings about obsolete options, use -Xlint:-options.
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:104: error: illegal start of type
    [javac]         if (toClass == null) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:104: error: <identifier> expected
    [javac]         if (toClass == null) {
    [javac]                    ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:109: error: illegal start of type
    [javac]         if (toClass.equals(type)) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:109: error: <identifier> expected
    [javac]         if (toClass.equals(type)) {
    [javac]                           ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:109: error: <identifier> expected
    [javac]         if (toClass.equals(type)) {
    [javac]                                ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:109: error: ';' expected
    [javac]         if (toClass.equals(type)) {
    [javac]                                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:113: error: illegal start of type
    [javac]         if (type instanceof Class<?>) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:113: error: <identifier> expected
    [javac]         if (type instanceof Class<?>) {
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:113: error: <identifier> expected
    [javac]         if (type instanceof Class<?>) {
    [javac]                                     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:118: error: illegal start of type
    [javac]         if (type instanceof ParameterizedType) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:118: error: <identifier> expected
    [javac]         if (type instanceof ParameterizedType) {
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:118: error: <identifier> expected
    [javac]         if (type instanceof ParameterizedType) {
    [javac]                                              ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:124: error: illegal start of type
    [javac]         if (type instanceof TypeVariable<?>) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:124: error: <identifier> expected
    [javac]         if (type instanceof TypeVariable<?>) {
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:124: error: <identifier> expected
    [javac]         if (type instanceof TypeVariable<?>) {
    [javac]                                            ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:138: error: illegal start of type
    [javac]         if (type instanceof GenericArrayType) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:138: error: <identifier> expected
    [javac]         if (type instanceof GenericArrayType) {
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:138: error: <identifier> expected
    [javac]         if (type instanceof GenericArrayType) {
    [javac]                                             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:147: error: illegal start of type
    [javac]         if (type instanceof WildcardType) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:147: error: <identifier> expected
    [javac]         if (type instanceof WildcardType) {
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:147: error: <identifier> expected
    [javac]         if (type instanceof WildcardType) {
    [javac]                                         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:151: error: illegal start of type
    [javac]         throw new IllegalStateException("found an unhandled type: " + type);
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:151: error: invalid method declaration; return type required
    [javac]         throw new IllegalStateException("found an unhandled type: " + type);
    [javac]                   ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:151: error: illegal start of type
    [javac]         throw new IllegalStateException("found an unhandled type: " + type);
    [javac]                                         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:163: error: class, interface, or enum expected
    [javac]     private static boolean isAssignable(Type type, ParameterizedType toParameterizedType,
    [javac]                    ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:167: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:173: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:178: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:184: error: class, interface, or enum expected
    [javac]         Map<TypeVariable<?>, Type> fromTypeVarAssigns = getTypeArguments(type, toClass, null);
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:187: error: class, interface, or enum expected
    [javac]         if (fromTypeVarAssigns == null) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:189: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:196: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:203: error: class, interface, or enum expected
    [javac]         for (Map.Entry<TypeVariable<?>, Type> entry : toTypeVarAssigns.entrySet()) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:205: error: class, interface, or enum expected
    [javac]             Type fromTypeArg = fromTypeVarAssigns.get(entry.getKey());
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:210: error: class, interface, or enum expected
    [javac]             if (fromTypeArg != null
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:215: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:219: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:223: error: class, interface, or enum expected
    [javac]         do {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:225: error: class, interface, or enum expected
    [javac]             if (result instanceof TypeVariable<?> && !result.equals(var)) {
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:227: error: class, interface, or enum expected
    [javac]                 continue;
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:228: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:230: error: class, interface, or enum expected
    [javac]         } while (true);
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:231: error: class, interface, or enum expected
    [javac]         return result;
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:232: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:248: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:254: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:259: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:263: error: class, interface, or enum expected
    [javac]         if (type instanceof Class<?>) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:267: error: class, interface, or enum expected
    [javac]             return cls.isArray()
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:269: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:275: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:282: error: class, interface, or enum expected
    [javac]                 }
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:286: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:294: error: class, interface, or enum expected
    [javac]                 }
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:298: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:305: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:308: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:324: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:330: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:335: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:338: error: class, interface, or enum expected
    [javac]         Type[] toLowerBounds = getImplicitLowerBounds(toWildcardType);
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:340: error: class, interface, or enum expected
    [javac]         if (type instanceof WildcardType) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:342: error: class, interface, or enum expected
    [javac]             Type[] upperBounds = getImplicitUpperBounds(wildcardType);
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:343: error: class, interface, or enum expected
    [javac]             Type[] lowerBounds = getImplicitLowerBounds(wildcardType);
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:345: error: class, interface, or enum expected
    [javac]             for (Type toBound : toUpperBounds) {
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:353: error: class, interface, or enum expected
    [javac]                 for (Type bound : upperBounds) {
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:356: error: class, interface, or enum expected
    [javac]                     }
    [javac]                     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:368: error: class, interface, or enum expected
    [javac]                 for (Type bound : lowerBounds) {
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:371: error: class, interface, or enum expected
    [javac]                     }
    [javac]                     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:376: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:384: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:393: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:397: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:413: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:419: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:424: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:432: error: class, interface, or enum expected
    [javac]             for (Type bound : bounds) {
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:435: error: class, interface, or enum expected
    [javac]                 }
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:442: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:445: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:459: error: class, interface, or enum expected
    [javac]             if (replacementType == null) {
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:462: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:465: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:468: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:481: error: class, interface, or enum expected
    [javac]     public static Map<TypeVariable<?>, Type> getTypeArguments(ParameterizedType type) {
    [javac]                   ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:483: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:517: error: class, interface, or enum expected
    [javac]     public static Map<TypeVariable<?>, Type> getTypeArguments(Type type, Class<?> toClass) {
    [javac]                   ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:519: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:533: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:537: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:542: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:551: error: class, interface, or enum expected
    [javac]                 }
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:555: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:563: error: class, interface, or enum expected
    [javac]                 }
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:567: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:571: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:587: error: class, interface, or enum expected
    [javac]         if (!isAssignable(cls, toClass)) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:589: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:592: error: class, interface, or enum expected
    [javac]         Map<TypeVariable<?>, Type> typeVarAssigns;
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:594: error: class, interface, or enum expected
    [javac]         if (ownerType instanceof ParameterizedType) {
    [javac]         ^
    [javac] 100 errors
    [javac] 4 warnings

BUILD FAILED
/ymy/test/Lang_15_buggy/build.xml:62: Compile failed; see the compiler error output for details.

Total time: 0 seconds
Cannot compile test suite! at /opt/defects4j/framework/bin/d4j/d4j-test line 134.
Compilation failed in require at /opt/defects4j/framework/bin/defects4j line 195.

## Lang_16
Lang_16: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 0

## Lang_17
Lang_17: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang3.text.translate.NumericEntityEscaperTest::testSupplementary

## Lang_19
Lang_19: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang3.text.translate.NumericEntityUnescaperTest::testUnfinishedEntity

## Lang_20
Lang_20: Running ant (compile.tests)................................................ FAIL
Executed command:  cd /ymy/test/Lang_20_buggy && /opt/defects4j/major/bin/ant -f /opt/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/opt/defects4j -Dd4j.dir.projects=/opt/defects4j/framework/projects -Dbasedir=/ymy/test/Lang_20_buggy  compile.tests 2>&1
Buildfile: /opt/defects4j/framework/projects/defects4j.build.xml

init:
     [echo] -------- commons-lang 3.0 --------
    [mkdir] Created dir: /ymy/test/Lang_20_buggy/target

compile:
    [mkdir] Created dir: /ymy/test/Lang_20_buggy/target/classes
    [javac] Compiling 99 source files to /ymy/test/Lang_20_buggy/target/classes
    [javac] warning: [options] bootstrap class path not set in conjunction with -source 6
    [javac] warning: [options] source value 6 is obsolete and will be removed in a future release
    [javac] warning: [options] target value 1.6 is obsolete and will be removed in a future release
    [javac] warning: [options] To suppress warnings about obsolete options, use -Xlint:-options.
    [javac] /ymy/test/Lang_20_buggy/src/main/java/org/apache/commons/lang3/StringUtils.java:3228: error: illegal start of type
    [javac]      */
    [javac]      ^
    [javac] 1 error
    [javac] 4 warnings

BUILD FAILED
/ymy/test/Lang_20_buggy/build.xml:63: Compile failed; see the compiler error output for details.

Total time: 0 seconds
Cannot compile test suite! at /opt/defects4j/framework/bin/d4j/d4j-test line 134.
Compilation failed in require at /opt/defects4j/framework/bin/defects4j line 195.

## Lang_21
Lang_21: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 0

## Lang_22
Lang_22: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 2
  - org.apache.commons.lang3.math.FractionTest::testReducedFactory_int_int
  - org.apache.commons.lang3.math.FractionTest::testReduce

## Lang_23
Lang_23: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang3.text.ExtendedMessageFormatTest::testEqualsHashcode

## Lang_24
Lang_24: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 0

## Lang_26
Lang_26: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang3.time.FastDateFormatTest::testLang645

## Lang_27
Lang_27: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang3.math.NumberUtilsTest::testCreateNumber

## Lang_28
Lang_28: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 0

## Lang_29
Lang_29: Running ant (compile.tests)................................................ FAIL
Executed command:  cd /ymy/test/Lang_29_buggy && /opt/defects4j/major/bin/ant -f /opt/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/opt/defects4j -Dd4j.dir.projects=/opt/defects4j/framework/projects -Dbasedir=/ymy/test/Lang_29_buggy  compile.tests 2>&1
Buildfile: /opt/defects4j/framework/projects/defects4j.build.xml

test-offline:

get-deps:

compile:
    [mkdir] Created dir: /ymy/test/Lang_29_buggy/target/classes
    [javac] /ymy/test/Lang_29_buggy/maven-build.xml:75: warning: 'includeantruntime' was not set, defaulting to build.sysclasspath=last; set to false for repeatable builds
    [javac] Compiling 88 source files to /ymy/test/Lang_29_buggy/target/classes
    [javac] warning: [options] bootstrap class path not set in conjunction with -source 6
    [javac] warning: [options] source value 6 is obsolete and will be removed in a future release
    [javac] warning: [options] target value 1.6 is obsolete and will be removed in a future release
    [javac] warning: [options] To suppress warnings about obsolete options, use -Xlint:-options.
    [javac] /ymy/test/Lang_29_buggy/src/main/java/org/apache/commons/lang3/SystemUtils.java:45: error: class, interface, or enum expected
    [javac]     static int toJavaVersionInt(String version) {
    [javac]            ^
    [javac] /ymy/test/Lang_29_buggy/src/main/java/org/apache/commons/lang3/SystemUtils.java:47: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] 2 errors
    [javac] 4 warnings

BUILD FAILED
/ymy/test/Lang_29_buggy/maven-build.xml:75: Compile failed; see the compiler error output for details.

Total time: 0 seconds
Cannot compile test suite! at /opt/defects4j/framework/bin/d4j/d4j-test line 134.
Compilation failed in require at /opt/defects4j/framework/bin/defects4j line 195.

## Lang_30
Lang_30: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 8
  - org.apache.commons.lang3.StringUtilsEqualsIndexOfTest::testContainsNone_CharArrayWithSupplementaryChars
  - org.apache.commons.lang3.StringUtilsEqualsIndexOfTest::testContainsNone_StringWithSupplementaryChars
  - org.apache.commons.lang3.StringUtilsEqualsIndexOfTest::testContainsAny_StringCharArrayWithBadSupplementaryChars
  - org.apache.commons.lang3.StringUtilsEqualsIndexOfTest::testIndexOfAnyBut_StringStringWithSupplementaryChars
  - org.apache.commons.lang3.StringUtilsEqualsIndexOfTest::testContainsAny_StringWithBadSupplementaryChars
  - org.apache.commons.lang3.StringUtilsEqualsIndexOfTest::testIndexOfAnyBut_StringCharArrayWithSupplementaryChars
  - org.apache.commons.lang3.StringUtilsEqualsIndexOfTest::testContainsNone_StringWithBadSupplementaryChars
  - org.apache.commons.lang3.StringUtilsEqualsIndexOfTest::testContainsNone_CharArrayWithBadSupplementaryChars

## Lang_31
Lang_31: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 0

## Lang_32
Lang_32: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 8
  - org.apache.commons.lang3.builder.HashCodeBuilderAndEqualsBuilderTest::testIntegerWithTransients
  - org.apache.commons.lang3.builder.HashCodeBuilderAndEqualsBuilderTest::testFixture
  - org.apache.commons.lang3.builder.HashCodeBuilderAndEqualsBuilderTest::testFixtureWithTransients
  - org.apache.commons.lang3.builder.HashCodeBuilderAndEqualsBuilderTest::testInteger
  - org.apache.commons.lang3.builder.HashCodeBuilderTest::testReflectionObjectCycle
  - org.apache.commons.lang3.builder.HashCodeBuilderTest::testReflectionHierarchyHashCode
  - org.apache.commons.lang3.builder.HashCodeBuilderTest::testReflectionHashCode
  - org.apache.commons.lang3.builder.HashCodeBuilderTest::testReflectionHashCodeExcludeFields

## Lang_33
Lang_33: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 0

## Lang_34
Lang_34: Running ant (compile.tests)................................................ FAIL
Executed command:  cd /ymy/test/Lang_34_buggy && /opt/defects4j/major/bin/ant -f /opt/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/opt/defects4j -Dd4j.dir.projects=/opt/defects4j/framework/projects -Dbasedir=/ymy/test/Lang_34_buggy  compile.tests 2>&1
Buildfile: /opt/defects4j/framework/projects/defects4j.build.xml

test-offline:

get-deps:

compile:
    [mkdir] Created dir: /ymy/test/Lang_34_buggy/target/classes
    [javac] /ymy/test/Lang_34_buggy/maven-build.xml:75: warning: 'includeantruntime' was not set, defaulting to build.sysclasspath=last; set to false for repeatable builds
    [javac] Compiling 80 source files to /ymy/test/Lang_34_buggy/target/classes
    [javac] warning: [options] bootstrap class path not set in conjunction with -source 6
    [javac] warning: [options] source value 6 is obsolete and will be removed in a future release
    [javac] warning: [options] target value 1.6 is obsolete and will be removed in a future release
    [javac] warning: [options] To suppress warnings about obsolete options, use -Xlint:-options.
    [javac] /ymy/test/Lang_34_buggy/src/main/java/org/apache/commons/lang3/builder/ToStringStyle.java:39: error: class, interface, or enum expected
    [javac]     static Map<Object, Object> getRegistry() {
    [javac]            ^
    [javac] /ymy/test/Lang_34_buggy/src/main/java/org/apache/commons/lang3/builder/ToStringStyle.java:41: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_34_buggy/src/main/java/org/apache/commons/lang3/builder/ToStringStyle.java:55: error: illegal start of type
    [javac]  *   protected void appendDetail(StringBuffer buffer, String fieldName, Object value) {
    [javac]  ^
    [javac] /ymy/test/Lang_34_buggy/src/main/java/org/apache/commons/lang3/builder/ToStringStyle.java:56: error: illegal start of expression
    [javac]  *     if (value instanceof Date) {
    [javac]  ^
    [javac] /ymy/test/Lang_34_buggy/src/main/java/org/apache/commons/lang3/builder/ToStringStyle.java:56: error: illegal start of expression
    [javac]  *     if (value instanceof Date) {
    [javac]        ^
    [javac] /ymy/test/Lang_34_buggy/src/main/java/org/apache/commons/lang3/builder/ToStringStyle.java:57: error: illegal start of expression
    [javac]  *       value = new SimpleDateFormat("yyyy-MM-dd").format(value);
    [javac]  ^
    [javac] /ymy/test/Lang_34_buggy/src/main/java/org/apache/commons/lang3/builder/ToStringStyle.java:58: error: illegal start of expression
    [javac]  *     }
    [javac]  ^
    [javac] /ymy/test/Lang_34_buggy/src/main/java/org/apache/commons/lang3/builder/ToStringStyle.java:58: error: illegal start of expression
    [javac]  *     }
    [javac]        ^
    [javac] /ymy/test/Lang_34_buggy/src/main/java/org/apache/commons/lang3/builder/ToStringStyle.java:59: error: illegal start of expression
    [javac]  *     buffer.append(value);
    [javac]  ^
    [javac] /ymy/test/Lang_34_buggy/src/main/java/org/apache/commons/lang3/builder/ToStringStyle.java:60: error: illegal start of expression
    [javac]  *   }
    [javac]  ^
    [javac] /ymy/test/Lang_34_buggy/src/main/java/org/apache/commons/lang3/builder/ToStringStyle.java:60: error: illegal start of expression
    [javac]  *   }
    [javac]      ^
    [javac] /ymy/test/Lang_34_buggy/src/main/java/org/apache/commons/lang3/builder/ToStringStyle.java:61: error: illegal start of type
    [javac]  * }
    [javac]  ^
    [javac] /ymy/test/Lang_34_buggy/src/main/java/org/apache/commons/lang3/builder/ToStringStyle.java:62: error: class, interface, or enum expected
    [javac]  * </pre>
    [javac]  ^
    [javac] /ymy/test/Lang_34_buggy/src/main/java/org/apache/commons/lang3/builder/ToStringStyle.java:65: error: class, interface, or enum expected
    [javac]  * @author Apache Software Foundation
    [javac]            ^
    [javac] /ymy/test/Lang_34_buggy/src/main/java/org/apache/commons/lang3/builder/ToStringStyle.java:66: error: class, interface, or enum expected
    [javac]  * @author Gary Gregory
    [javac]            ^
    [javac] /ymy/test/Lang_34_buggy/src/main/java/org/apache/commons/lang3/builder/ToStringStyle.java:67: error: class, interface, or enum expected
    [javac]  * @author Pete Gieser
    [javac]            ^
    [javac] /ymy/test/Lang_34_buggy/src/main/java/org/apache/commons/lang3/builder/ToStringStyle.java:68: error: class, interface, or enum expected
    [javac]  * @author Masato Tezuka
    [javac]            ^
    [javac] /ymy/test/Lang_34_buggy/src/main/java/org/apache/commons/lang3/builder/ToStringStyle.java:69: error: class, interface, or enum expected
    [javac]  * @since 1.0
    [javac]           ^
    [javac] /ymy/test/Lang_34_buggy/src/main/java/org/apache/commons/lang3/builder/ToStringStyle.java:70: error: class, interface, or enum expected
    [javac]  * @version $Id$
    [javac]             ^
    [javac] 19 errors
    [javac] 4 warnings

BUILD FAILED
/ymy/test/Lang_34_buggy/maven-build.xml:75: Compile failed; see the compiler error output for details.

Total time: 0 seconds
Cannot compile test suite! at /opt/defects4j/framework/bin/d4j/d4j-test line 134.
Compilation failed in require at /opt/defects4j/framework/bin/defects4j line 195.

## Lang_35
Lang_35: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang3.ArrayUtilsAddTest::testLANG571

## Lang_36
Lang_36: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang3.math.NumberUtilsTest::testIsNumber

## Lang_37
Lang_37: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 0

## Lang_38
Lang_38: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 7
  - org.apache.commons.lang3.time.DateFormatUtilsTest::testTimeISO
  - org.apache.commons.lang3.time.DateFormatUtilsTest::testSMTP
  - org.apache.commons.lang3.time.DateFormatUtilsTest::testDateTimeISO
  - org.apache.commons.lang3.time.DateFormatUtilsTest::testTimeNoTISO
  - org.apache.commons.lang3.time.DateFormatUtilsTest::testDateISO
  - org.apache.commons.lang3.time.DurationFormatUtilsTest::testFormatPeriodISO
  - org.apache.commons.lang3.time.FastDateFormatTest::testLang538

## Lang_39
Lang_39: Running ant (compile.tests)................................................ FAIL
Executed command:  cd /ymy/test/Lang_39_buggy && /opt/defects4j/major/bin/ant -f /opt/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/opt/defects4j -Dd4j.dir.projects=/opt/defects4j/framework/projects -Dbasedir=/ymy/test/Lang_39_buggy  compile.tests 2>&1
Buildfile: /opt/defects4j/framework/projects/defects4j.build.xml

test-offline:

get-deps:

compile:
    [mkdir] Created dir: /ymy/test/Lang_39_buggy/target/classes
    [javac] /ymy/test/Lang_39_buggy/maven-build.xml:74: warning: 'includeantruntime' was not set, defaulting to build.sysclasspath=last; set to false for repeatable builds
    [javac] Compiling 79 source files to /ymy/test/Lang_39_buggy/target/classes
    [javac] warning: [options] bootstrap class path not set in conjunction with -source 6
    [javac] warning: [options] source value 6 is obsolete and will be removed in a future release
    [javac] warning: [options] target value 1.6 is obsolete and will be removed in a future release
    [javac] warning: [options] To suppress warnings about obsolete options, use -Xlint:-options.
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:24: error: class, interface, or enum expected
    [javac] private static String replaceEach(String text, String[] searchList, String[] replacementList, 
    [javac]                ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:31: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:35: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:38: error: class, interface, or enum expected
    [javac]     int replacementLength = replacementList.length;
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:40: error: class, interface, or enum expected
    [javac]     if (searchLength != replacementLength) {
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:45: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:49: error: class, interface, or enum expected
    [javac]     int textIndex = -1;
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:50: error: class, interface, or enum expected
    [javac]     int replaceIndex = -1;
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:51: error: class, interface, or enum expected
    [javac]     int tempIndex = -1;
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:53: error: class, interface, or enum expected
    [javac]     for (int i = 0; i < searchLength; i++) {
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:53: error: class, interface, or enum expected
    [javac]     for (int i = 0; i < searchLength; i++) {
    [javac]                     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:53: error: class, interface, or enum expected
    [javac]     for (int i = 0; i < searchLength; i++) {
    [javac]                                       ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:58: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:61: error: class, interface, or enum expected
    [javac]         if (tempIndex == -1) {
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:63: error: class, interface, or enum expected
    [javac]         } else {
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:66: error: class, interface, or enum expected
    [javac]                 replaceIndex = i;
    [javac]                 ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:67: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:73: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:76: error: class, interface, or enum expected
    [javac]     int increase = 0;
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:78: error: class, interface, or enum expected
    [javac]     for (int i = 0; i < searchList.length; i++) {
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:78: error: class, interface, or enum expected
    [javac]     for (int i = 0; i < searchList.length; i++) {
    [javac]                     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:78: error: class, interface, or enum expected
    [javac]     for (int i = 0; i < searchList.length; i++) {
    [javac]                                            ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:81: error: class, interface, or enum expected
    [javac]             if (greater > 0) {
    [javac]             ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:83: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:88: error: class, interface, or enum expected
    [javac]     StringBuilder buf = new StringBuilder(text.length() + increase);
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:90: error: class, interface, or enum expected
    [javac]     while (textIndex != -1) {
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:91: error: class, interface, or enum expected
    [javac]         for (int i = start; i < textIndex; i++) {
    [javac]                             ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:91: error: class, interface, or enum expected
    [javac]         for (int i = start; i < textIndex; i++) {
    [javac]                                            ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:93: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:96: error: class, interface, or enum expected
    [javac]         } else {
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:98: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:102: error: class, interface, or enum expected
    [javac]         textIndex = -1;
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:103: error: class, interface, or enum expected
    [javac]         replaceIndex = -1;
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:104: error: class, interface, or enum expected
    [javac]         tempIndex = -1;
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:105: error: class, interface, or enum expected
    [javac]         for (int i = 0; i < searchLength; i++) {
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:105: error: class, interface, or enum expected
    [javac]         for (int i = 0; i < searchLength; i++) {
    [javac]                         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:105: error: class, interface, or enum expected
    [javac]         for (int i = 0; i < searchLength; i++) {
    [javac]                                           ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:110: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:113: error: class, interface, or enum expected
    [javac]             if (tempIndex == -1) {
    [javac]             ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:115: error: class, interface, or enum expected
    [javac]             } else {
    [javac]             ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:118: error: class, interface, or enum expected
    [javac]                     replaceIndex = i;
    [javac]                     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:119: error: class, interface, or enum expected
    [javac]                 }
    [javac]                 ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:124: error: class, interface, or enum expected
    [javac]     for (int i = start; i < textLength; i++) {
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:124: error: class, interface, or enum expected
    [javac]     for (int i = start; i < textLength; i++) {
    [javac]                         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:124: error: class, interface, or enum expected
    [javac]     for (int i = start; i < textLength; i++) {
    [javac]                                         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:126: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:128: error: class, interface, or enum expected
    [javac]     if (!repeat) {
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:130: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:133: error: class, interface, or enum expected
    [javac] }
    [javac] ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:140: error: class, interface, or enum expected
    [javac]      * @param str  the String to check, may be null
    [javac]               ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:141: error: <identifier> expected
    [javac]      * @return <code>true</code> if the String is not empty and not null
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:143: error: class, interface, or enum expected
    [javac]     public static boolean isNotEmpty(CharSequence str) {
    [javac]                   ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:145: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:162: error: class, interface, or enum expected
    [javac]     public static boolean isBlank(CharSequence str) {
    [javac]                   ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:164: error: class, interface, or enum expected
    [javac]         if (str == null || (strLen = str.length()) == 0) {
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:166: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:167: error: class, interface, or enum expected
    [javac]         for (int i = 0; i < strLen; i++) {
    [javac]                         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:167: error: class, interface, or enum expected
    [javac]         for (int i = 0; i < strLen; i++) {
    [javac]                                     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:170: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:173: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:191: error: class, interface, or enum expected
    [javac]     public static boolean isNotBlank(CharSequence str) {
    [javac]                   ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:193: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:220: error: class, interface, or enum expected
    [javac]     public static String trim(String str) {
    [javac]                   ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:222: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:246: error: class, interface, or enum expected
    [javac]     public static String trimToNull(String str) {
    [javac]                   ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:248: error: class, interface, or enum expected
    [javac]         return isEmpty(ts) ? null : ts;
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:249: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:272: error: class, interface, or enum expected
    [javac]     public static String trimToEmpty(String str) {
    [javac]                   ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:274: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:300: error: class, interface, or enum expected
    [javac]     public static String strip(String str) {
    [javac]                   ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:302: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:327: error: class, interface, or enum expected
    [javac]     public static String stripToNull(String str) {
    [javac]                   ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:330: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:332: error: class, interface, or enum expected
    [javac]         return str.length() == 0 ? null : str;
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:333: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:357: error: class, interface, or enum expected
    [javac]     public static String stripToEmpty(String str) {
    [javac]                   ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:359: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:387: error: class, interface, or enum expected
    [javac]     public static String strip(String str, String stripChars) {
    [javac]                   ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:390: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:392: error: class, interface, or enum expected
    [javac]         return stripEnd(str, stripChars);
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:393: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:419: error: class, interface, or enum expected
    [javac]     public static String stripStart(String str, String stripChars) {
    [javac]                   ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:421: error: class, interface, or enum expected
    [javac]         if (str == null || (strLen = str.length()) == 0) {
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:423: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:425: error: class, interface, or enum expected
    [javac]         if (stripChars == null) {
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:428: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:431: error: class, interface, or enum expected
    [javac]         } else {
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:434: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:437: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:463: error: class, interface, or enum expected
    [javac]     public static String stripEnd(String str, String stripChars) {
    [javac]                   ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:465: error: class, interface, or enum expected
    [javac]         if (str == null || (end = str.length()) == 0) {
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:467: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:472: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:475: error: class, interface, or enum expected
    [javac]         } else {
    [javac]         ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:478: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:481: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:504: error: class, interface, or enum expected
    [javac]     public static String[] stripAll(String[] strs) {
    [javac]                   ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:506: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:533: error: class, interface, or enum expected
    [javac]     public static String[] stripAll(String[] strs, String stripChars) {
    [javac]                   ^
    [javac] /ymy/test/Lang_39_buggy/src/java/org/apache/commons/lang3/StringUtils.java:535: error: class, interface, or enum expected
    [javac]         if (strs == null || (strsLen = strs.length) == 0) {
    [javac]         ^
    [javac] 100 errors
    [javac] 4 warnings

BUILD FAILED
/ymy/test/Lang_39_buggy/maven-build.xml:74: Compile failed; see the compiler error output for details.

Total time: 0 seconds
Cannot compile test suite! at /opt/defects4j/framework/bin/d4j/d4j-test line 134.
Compilation failed in require at /opt/defects4j/framework/bin/defects4j line 195.

## Lang_40
Lang_40: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang.StringUtilsEqualsIndexOfTest::testContainsIgnoreCase_LocaleIndependence

## Lang_41
Lang_41: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 2
  - org.apache.commons.lang.ClassUtilsTest::test_getShortClassName_Class
  - org.apache.commons.lang.ClassUtilsTest::test_getPackageName_Class

## Lang_42
Lang_42: Running ant (compile.tests)................................................ FAIL
Executed command:  cd /ymy/test/Lang_42_buggy && /opt/defects4j/major/bin/ant -f /opt/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/opt/defects4j -Dd4j.dir.projects=/opt/defects4j/framework/projects -Dbasedir=/ymy/test/Lang_42_buggy  compile.tests 2>&1
Buildfile: /opt/defects4j/framework/projects/defects4j.build.xml

init:
     [echo] -------- commons-lang 3.0-SNAPSHOT --------

prepare:
    [mkdir] Created dir: /ymy/test/Lang_42_buggy/target
    [mkdir] Created dir: /ymy/test/Lang_42_buggy/target/classes
    [mkdir] Created dir: /ymy/test/Lang_42_buggy/target/conf
    [mkdir] Created dir: /ymy/test/Lang_42_buggy/target/tests

static:
     [copy] Copying 1 file to /ymy/test/Lang_42_buggy/target/conf

compile:
    [javac] /ymy/test/Lang_42_buggy/build.xml:65: warning: 'includeantruntime' was not set, defaulting to build.sysclasspath=last; set to false for repeatable builds
    [javac] Compiling 85 source files to /ymy/test/Lang_42_buggy/target/classes
    [javac] warning: [options] bootstrap class path not set in conjunction with -source 6
    [javac] warning: [options] source value 6 is obsolete and will be removed in a future release
    [javac] warning: [options] target value 1.6 is obsolete and will be removed in a future release
    [javac] warning: [options] To suppress warnings about obsolete options, use -Xlint:-options.
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:27: error: class, interface, or enum expected
    [javac] public void escape(Writer writer, String str) throws IOException {
    [javac]        ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:29: error: class, interface, or enum expected
    [javac]     for (int i = 0; i < len; i++) {
    [javac]     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:29: error: class, interface, or enum expected
    [javac]     for (int i = 0; i < len; i++) {
    [javac]                     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:29: error: class, interface, or enum expected
    [javac]     for (int i = 0; i < len; i++) {
    [javac]                              ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:31: error: class, interface, or enum expected
    [javac]         if (Character.isHighSurrogate(c)) {
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:34: error: class, interface, or enum expected
    [javac]                 if (Character.isLowSurrogate(low)) {
    [javac]                 ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:36: error: class, interface, or enum expected
    [javac]                     writer.write("&#");
    [javac]                     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:37: error: class, interface, or enum expected
    [javac]                     writer.write(Integer.toString(codePoint, 10));
    [javac]                     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:38: error: class, interface, or enum expected
    [javac]                     writer.write(';');
    [javac]                     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:39: error: class, interface, or enum expected
    [javac]                     i++; // skip the low surrogate
    [javac]                     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:40: error: class, interface, or enum expected
    [javac]                     continue;
    [javac]                     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:41: error: class, interface, or enum expected
    [javac]                 }
    [javac]                 ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:45: error: class, interface, or enum expected
    [javac]         if (entityName == null) {
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:48: error: class, interface, or enum expected
    [javac]                 writer.write(Integer.toString(c, 10));
    [javac]                 ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:49: error: class, interface, or enum expected
    [javac]                 writer.write(';');
    [javac]                 ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:50: error: class, interface, or enum expected
    [javac]             } else {
    [javac]             ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:52: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:55: error: class, interface, or enum expected
    [javac]             writer.write(entityName);
    [javac]             ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:56: error: class, interface, or enum expected
    [javac]             writer.write(';');
    [javac]             ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:57: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:151: error: class, interface, or enum expected
    [javac]     static final String[][] HTML40_ARRAY = {
    [javac]                  ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:353: error: class, interface, or enum expected
    [javac]     public static final Entities XML;
    [javac]                         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:360: error: class, interface, or enum expected
    [javac]     public static final Entities HTML32;
    [javac]                         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:367: error: class, interface, or enum expected
    [javac]     public static final Entities HTML40;
    [javac]                         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:369: error: class, interface, or enum expected
    [javac]     static {
    [javac]            ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:371: error: class, interface, or enum expected
    [javac]         XML.addEntities(BASIC_ARRAY);
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:372: error: class, interface, or enum expected
    [javac]         XML.addEntities(APOS_ARRAY);
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:373: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:377: error: class, interface, or enum expected
    [javac]         HTML32.addEntities(BASIC_ARRAY);
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:378: error: class, interface, or enum expected
    [javac]         HTML32.addEntities(ISO8859_1_ARRAY);
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:379: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:383: error: class, interface, or enum expected
    [javac]         fillWithHtml40Entities(HTML40);
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:384: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:396: error: class, interface, or enum expected
    [javac]         entities.addEntities(ISO8859_1_ARRAY);
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:397: error: class, interface, or enum expected
    [javac]         entities.addEntities(HTML40_ARRAY);
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:398: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:722: error: class, interface, or enum expected
    [javac]     EntityMap map = new Entities.LookupEntityMap();
    [javac]     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:732: error: class, interface, or enum expected
    [javac]     public void addEntities(String[][] entityArray) {
    [javac]            ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:733: error: class, interface, or enum expected
    [javac]         for (int i = 0; i < entityArray.length; ++i) {
    [javac]                         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:733: error: class, interface, or enum expected
    [javac]         for (int i = 0; i < entityArray.length; ++i) {
    [javac]                                                 ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:735: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:748: error: class, interface, or enum expected
    [javac]     public void addEntity(String name, int value) {
    [javac]            ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:750: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:761: error: class, interface, or enum expected
    [javac]     public String entityName(int value) {
    [javac]            ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:763: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:774: error: class, interface, or enum expected
    [javac]     public int entityValue(String name) {
    [javac]            ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:776: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:792: error: class, interface, or enum expected
    [javac]     public String escape(String str) {
    [javac]            ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:794: error: class, interface, or enum expected
    [javac]         try {
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:796: error: class, interface, or enum expected
    [javac]         } catch (IOException e) {
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:800: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:802: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:821: error: class, interface, or enum expected
    [javac]     public void escape(Writer writer, String str) throws IOException {
    [javac]            ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:823: error: class, interface, or enum expected
    [javac]         for (int i = 0; i < len; i++) {
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:823: error: class, interface, or enum expected
    [javac]         for (int i = 0; i < len; i++) {
    [javac]                         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:823: error: class, interface, or enum expected
    [javac]         for (int i = 0; i < len; i++) {
    [javac]                                  ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:825: error: class, interface, or enum expected
    [javac]             String entityName = this.entityName(c);
    [javac]             ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:826: error: class, interface, or enum expected
    [javac]             if (entityName == null) {
    [javac]             ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:829: error: class, interface, or enum expected
    [javac]                     writer.write(Integer.toString(c, 10));
    [javac]                     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:830: error: class, interface, or enum expected
    [javac]                     writer.write(';');
    [javac]                     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:831: error: class, interface, or enum expected
    [javac]                 } else {
    [javac]                 ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:833: error: class, interface, or enum expected
    [javac]                 }
    [javac]                 ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:836: error: class, interface, or enum expected
    [javac]                 writer.write(entityName);
    [javac]                 ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:837: error: class, interface, or enum expected
    [javac]                 writer.write(';');
    [javac]                 ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:838: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:856: error: class, interface, or enum expected
    [javac]     public String unescape(String str) {
    [javac]            ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:858: error: class, interface, or enum expected
    [javac]         if (firstAmp < 0) {
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:860: error: class, interface, or enum expected
    [javac]         } else {
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:862: error: class, interface, or enum expected
    [javac]             try {
    [javac]             ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:864: error: class, interface, or enum expected
    [javac]             } catch (IOException e) {
    [javac]             ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:868: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:870: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:881: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:900: error: class, interface, or enum expected
    [javac]     public void unescape(Writer writer, String str) throws IOException {
    [javac]            ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:902: error: class, interface, or enum expected
    [javac]         if (firstAmp < 0) {
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:904: error: class, interface, or enum expected
    [javac]             return;
    [javac]             ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:905: error: class, interface, or enum expected
    [javac]         } else {
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:907: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:925: error: class, interface, or enum expected
    [javac]         int len = str.length();
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:926: error: class, interface, or enum expected
    [javac]         for (int i = firstAmp; i < len; i++) {
    [javac]         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:926: error: class, interface, or enum expected
    [javac]         for (int i = firstAmp; i < len; i++) {
    [javac]                                ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:926: error: class, interface, or enum expected
    [javac]         for (int i = firstAmp; i < len; i++) {
    [javac]                                         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:928: error: class, interface, or enum expected
    [javac]             if (c == '&') {
    [javac]             ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:930: error: class, interface, or enum expected
    [javac]                 int semiColonIdx = str.indexOf(';', nextIdx);
    [javac]                 ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:931: error: class, interface, or enum expected
    [javac]                 if (semiColonIdx == -1) {
    [javac]                 ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:933: error: class, interface, or enum expected
    [javac]                     continue;
    [javac]                     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:934: error: class, interface, or enum expected
    [javac]                 }
    [javac]                 ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:936: error: class, interface, or enum expected
    [javac]                 if (amphersandIdx != -1 && amphersandIdx < semiColonIdx) {
    [javac]                 ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:939: error: class, interface, or enum expected
    [javac]                     continue;
    [javac]                     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:940: error: class, interface, or enum expected
    [javac]                 }
    [javac]                 ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:942: error: class, interface, or enum expected
    [javac]                 int entityValue = -1;
    [javac]                 ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:943: error: class, interface, or enum expected
    [javac]                 int entityContentLen = entityContent.length();
    [javac]                 ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:944: error: class, interface, or enum expected
    [javac]                 if (entityContentLen > 0) {
    [javac]                 ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:949: error: class, interface, or enum expected
    [javac]                             try {
    [javac]                             ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:954: error: class, interface, or enum expected
    [javac]                                         break;
    [javac]                                         ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:955: error: class, interface, or enum expected
    [javac]                                     }
    [javac]                                     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:958: error: class, interface, or enum expected
    [javac]                                     }
    [javac]                                     ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:962: error: class, interface, or enum expected
    [javac]                                 }
    [javac]                                 ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:965: error: class, interface, or enum expected
    [javac]                             }
    [javac]                             ^
    [javac] /ymy/test/Lang_42_buggy/src/java/org/apache/commons/lang/Entities.java:969: error: class, interface, or enum expected
    [javac]                     }
    [javac]                     ^
    [javac] 100 errors
    [javac] 4 warnings

BUILD FAILED
/ymy/test/Lang_42_buggy/build.xml:65: Compile failed; see the compiler error output for details.

Total time: 1 second
Cannot compile test suite! at /opt/defects4j/framework/bin/d4j/d4j-test line 134.
Compilation failed in require at /opt/defects4j/framework/bin/defects4j line 195.

## Lang_43
Lang_43: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang.text.ExtendedMessageFormatTest::testEscapedQuote_LANG_477

## Lang_44
Lang_44: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 0

## Lang_45
Lang_45: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 0

## Lang_46
Lang_46: Running ant (compile.tests)................................................ FAIL
Executed command:  cd /ymy/test/Lang_46_buggy && /opt/defects4j/major/bin/ant -f /opt/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/opt/defects4j -Dd4j.dir.projects=/opt/defects4j/framework/projects -Dbasedir=/ymy/test/Lang_46_buggy  compile.tests 2>&1
Buildfile: /opt/defects4j/framework/projects/defects4j.build.xml

init:
     [echo] -------- commons-lang 3.0-SNAPSHOT --------

prepare:
    [mkdir] Created dir: /ymy/test/Lang_46_buggy/target
    [mkdir] Created dir: /ymy/test/Lang_46_buggy/target/classes
    [mkdir] Created dir: /ymy/test/Lang_46_buggy/target/conf
    [mkdir] Created dir: /ymy/test/Lang_46_buggy/target/tests

static:
     [copy] Copying 1 file to /ymy/test/Lang_46_buggy/target/conf

compile:
    [javac] /ymy/test/Lang_46_buggy/build.xml:65: warning: 'includeantruntime' was not set, defaulting to build.sysclasspath=last; set to false for repeatable builds
    [javac] Compiling 80 source files to /ymy/test/Lang_46_buggy/target/classes
    [javac] warning: [options] bootstrap class path not set in conjunction with -source 6
    [javac] warning: [options] source value 6 is obsolete and will be removed in a future release
    [javac] warning: [options] target value 1.6 is obsolete and will be removed in a future release
    [javac] warning: [options] To suppress warnings about obsolete options, use -Xlint:-options.
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:2334: warning: [deprecation] Character(char) in Character has been deprecated
    [javac]             result[i] = new Character(array[i]);
    [javac]                         ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:2402: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]             result[i] = new Long(array[i]);
    [javac]                         ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:2470: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]             result[i] = new Integer(array[i]);
    [javac]                         ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:2538: warning: [deprecation] Short(short) in Short has been deprecated
    [javac]             result[i] = new Short(array[i]);
    [javac]                         ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:2606: warning: [deprecation] Byte(byte) in Byte has been deprecated
    [javac]             result[i] = new Byte(array[i]);
    [javac]                         ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:2674: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]             result[i] = new Double(array[i]);
    [javac]                         ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:2742: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]             result[i] = new Float(array[i]);
    [javac]                         ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:3573: warning: [deprecation] Character(char) in Character has been deprecated
    [javac]         return (char[]) add(array, index, new Character(element), Character.TYPE);
    [javac]                                           ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:3604: warning: [deprecation] Byte(byte) in Byte has been deprecated
    [javac]         return (byte[]) add(array, index, new Byte(element), Byte.TYPE);
    [javac]                                           ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:3635: warning: [deprecation] Short(short) in Short has been deprecated
    [javac]         return (short[]) add(array, index, new Short(element), Short.TYPE);
    [javac]                                            ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:3666: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]         return (int[]) add(array, index, new Integer(element), Integer.TYPE);
    [javac]                                          ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:3697: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]         return (long[]) add(array, index, new Long(element), Long.TYPE);
    [javac]                                           ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:3728: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]         return (float[]) add(array, index, new Float(element), Float.TYPE);
    [javac]                                            ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:3759: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]         return (double[]) add(array, index, new Double(element), Double.TYPE);
    [javac]                                             ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/CharUtils.java:75: warning: [deprecation] Character(char) in Character has been deprecated
    [javac]             CHAR_ARRAY[i] = new Character((char) i);
    [javac]                             ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/CharUtils.java:109: warning: [deprecation] Character(char) in Character has been deprecated
    [javac]         return new Character(ch);
    [javac]                ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/Entities.java:449: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]             mapNameToValue.put(name, new Integer(value));
    [javac]                                      ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/Entities.java:481: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]             mapNameToValue.put(name, new Integer(value));
    [javac]                                      ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/Entities.java:482: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]             mapValueToName.put(new Integer(value), name);
    [javac]                                ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/Entities.java:489: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]             return (String) mapValueToName.get(new Integer(value));
    [javac]                                                ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:86: error: incompatible types: String cannot be converted to Writer
    [javac]         return escapeJavaStyleString(str, false, false);
    [javac]                                      ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/builder/HashCodeBuilder.java:521: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]         return new Integer(System.identityHashCode(value));
    [javac]                ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/builder/ToStringBuilder.java:948: warning: [deprecation] appendIdentityToString(StringBuffer,Object) in ObjectUtils has been deprecated
    [javac]         ObjectUtils.appendIdentityToString(this.getStringBuffer(), object);
    [javac]                    ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/builder/ToStringStyle.java:565: warning: [deprecation] appendIdentityToString(StringBuffer,Object) in ObjectUtils has been deprecated
    [javac]        ObjectUtils.appendIdentityToString(buffer, value);
    [javac]                   ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/enums/Enum.java:662: warning: non-varargs call of varargs method with inexact argument type for last parameter;
    [javac]             Method mth = other.getClass().getMethod("getName", null);
    [javac]                                                                ^
    [javac]   cast to Class<?> for a varargs call
    [javac]   cast to Class<?>[] for a non-varargs call and to suppress this warning
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/enums/Enum.java:663: warning: non-varargs call of varargs method with inexact argument type for last parameter;
    [javac]             String name = (String) mth.invoke(other, null);
    [javac]                                                      ^
    [javac]   cast to Object for a varargs call
    [javac]   cast to Object[] for a non-varargs call and to suppress this warning
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/enums/ValuedEnum.java:209: warning: non-varargs call of varargs method with inexact argument type for last parameter;
    [javac]             Method mth = other.getClass().getMethod("getValue", null);
    [javac]                                                                 ^
    [javac]   cast to Class<?> for a varargs call
    [javac]   cast to Class<?>[] for a non-varargs call and to suppress this warning
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/enums/ValuedEnum.java:210: warning: non-varargs call of varargs method with inexact argument type for last parameter;
    [javac]             Integer value = (Integer) mth.invoke(other, null);
    [javac]                                                         ^
    [javac]   cast to Object for a varargs call
    [javac]   cast to Object[] for a non-varargs call and to suppress this warning
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/exception/ExceptionUtils.java:90: warning: non-varargs call of varargs method with inexact argument type for last parameter;
    [javac]             causeMethod = Throwable.class.getMethod("getCause", null);
    [javac]                                                                 ^
    [javac]   cast to Class<?> for a varargs call
    [javac]   cast to Class<?>[] for a non-varargs call and to suppress this warning
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/exception/ExceptionUtils.java:383: warning: non-varargs call of varargs method with inexact argument type for last parameter;
    [javac]             method = throwable.getClass().getMethod(methodName, null);
    [javac]                                                                 ^
    [javac]   cast to Class<?> for a varargs call
    [javac]   cast to Class<?>[] for a non-varargs call and to suppress this warning
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/exception/ExceptionUtils.java:474: warning: non-varargs call of varargs method with inexact argument type for last parameter;
    [javac]                     Method method = cls.getMethod(CAUSE_METHOD_NAMES[i], null);
    [javac]                                                                          ^
    [javac]   cast to Class for a varargs call
    [javac]   cast to Class[] for a non-varargs call and to suppress this warning
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/DoubleRange.java:182: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]             minObject = new Double(min);            
    [javac]                         ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/DoubleRange.java:236: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]             maxObject = new Double(max);            
    [javac]                         ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/FloatRange.java:182: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]             minObject = new Float(min);            
    [javac]                         ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/FloatRange.java:234: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]             maxObject = new Float(max);            
    [javac]                         ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/IntRange.java:165: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]             minObject = new Integer(min);            
    [javac]                         ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/IntRange.java:213: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]             maxObject = new Integer(max);            
    [javac]                         ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/LongRange.java:166: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]             minObject = new Long(min);            
    [javac]                         ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/LongRange.java:220: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]             maxObject = new Long(max);            
    [javac]                         ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:41: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]     public static final Long LONG_ZERO = new Long(0L);
    [javac]                                          ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:43: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]     public static final Long LONG_ONE = new Long(1L);
    [javac]                                         ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:45: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]     public static final Long LONG_MINUS_ONE = new Long(-1L);
    [javac]                                               ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:47: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]     public static final Integer INTEGER_ZERO = new Integer(0);
    [javac]                                                ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:49: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]     public static final Integer INTEGER_ONE = new Integer(1);
    [javac]                                               ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:51: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]     public static final Integer INTEGER_MINUS_ONE = new Integer(-1);
    [javac]                                                     ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:53: warning: [deprecation] Short(short) in Short has been deprecated
    [javac]     public static final Short SHORT_ZERO = new Short((short) 0);
    [javac]                                            ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:55: warning: [deprecation] Short(short) in Short has been deprecated
    [javac]     public static final Short SHORT_ONE = new Short((short) 1);
    [javac]                                           ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:57: warning: [deprecation] Short(short) in Short has been deprecated
    [javac]     public static final Short SHORT_MINUS_ONE = new Short((short) -1);
    [javac]                                                 ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:59: warning: [deprecation] Byte(byte) in Byte has been deprecated
    [javac]     public static final Byte BYTE_ZERO = new Byte((byte) 0);
    [javac]                                          ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:61: warning: [deprecation] Byte(byte) in Byte has been deprecated
    [javac]     public static final Byte BYTE_ONE = new Byte((byte) 1);
    [javac]                                         ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:63: warning: [deprecation] Byte(byte) in Byte has been deprecated
    [javac]     public static final Byte BYTE_MINUS_ONE = new Byte((byte) -1);
    [javac]                                               ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:65: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]     public static final Double DOUBLE_ZERO = new Double(0.0d);
    [javac]                                              ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:67: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]     public static final Double DOUBLE_ONE = new Double(1.0d);
    [javac]                                             ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:69: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]     public static final Double DOUBLE_MINUS_ONE = new Double(-1.0d);
    [javac]                                                   ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:71: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]     public static final Float FLOAT_ZERO = new Float(0.0f);
    [javac]                                            ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:73: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]     public static final Float FLOAT_ONE = new Float(1.0f);
    [javac]                                           ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:75: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]     public static final Float FLOAT_MINUS_ONE = new Float(-1.0f);
    [javac]                                                 ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/mutable/MutableByte.java:76: warning: [deprecation] Byte(byte) in Byte has been deprecated
    [javac]         return new Byte(this.value);
    [javac]                ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/mutable/MutableByte.java:157: warning: [deprecation] Byte(byte) in Byte has been deprecated
    [javac]         return new Byte(byteValue());
    [javac]                ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/mutable/MutableDouble.java:78: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]         return new Double(this.value);
    [javac]                ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/mutable/MutableDouble.java:168: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]         return new Double(doubleValue());
    [javac]                ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/mutable/MutableFloat.java:78: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]         return new Float(this.value);
    [javac]                ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/mutable/MutableFloat.java:240: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]         return new Float(floatValue());
    [javac]                ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/mutable/MutableInt.java:76: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]         return new Integer(this.value);
    [javac]                ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/mutable/MutableInt.java:220: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]         return new Integer(intValue());
    [javac]                ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/mutable/MutableLong.java:76: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]         return new Long(this.value);
    [javac]                ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/mutable/MutableLong.java:220: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]         return new Long(longValue());
    [javac]                ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/mutable/MutableShort.java:76: warning: [deprecation] Short(short) in Short has been deprecated
    [javac]         return new Short(this.value);
    [javac]                ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/mutable/MutableShort.java:229: warning: [deprecation] Short(short) in Short has been deprecated
    [javac]         return new Short(shortValue());
    [javac]                ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/oldenum/Enum.java:616: warning: non-varargs call of varargs method with inexact argument type for last parameter;
    [javac]             Method mth = other.getClass().getMethod("getName", null);
    [javac]                                                                ^
    [javac]   cast to Class<?> for a varargs call
    [javac]   cast to Class<?>[] for a non-varargs call and to suppress this warning
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/oldenum/Enum.java:617: warning: non-varargs call of varargs method with inexact argument type for last parameter;
    [javac]             String name = (String) mth.invoke(other, null);
    [javac]                                                      ^
    [javac]   cast to Object for a varargs call
    [javac]   cast to Object[] for a non-varargs call and to suppress this warning
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/time/FastDateFormat.java:280: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]         Object key = new Integer(style);
    [javac]                      ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/time/FastDateFormat.java:365: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]         Object key = new Integer(style);
    [javac]                      ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/time/FastDateFormat.java:459: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]         Object key = new Pair(new Integer(dateStyle), new Integer(timeStyle));
    [javac]                               ^
    [javac] /ymy/test/Lang_46_buggy/src/java/org/apache/commons/lang/time/FastDateFormat.java:459: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]         Object key = new Pair(new Integer(dateStyle), new Integer(timeStyle));
    [javac]                                                       ^
    [javac] Note: Some input files use unchecked or unsafe operations.
    [javac] Note: Recompile with -Xlint:unchecked for details.
    [javac] Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output
    [javac] 1 error
    [javac] 78 warnings

BUILD FAILED
/ymy/test/Lang_46_buggy/build.xml:65: Compile failed; see the compiler error output for details.

Total time: 2 seconds
Cannot compile test suite! at /opt/defects4j/framework/bin/d4j/d4j-test line 134.
Compilation failed in require at /opt/defects4j/framework/bin/defects4j line 195.

## Lang_47
Lang_47: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 2
  - org.apache.commons.lang.text.StrBuilderTest::testLang412Left
  - org.apache.commons.lang.text.StrBuilderTest::testLang412Right

## Lang_49
Lang_49: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 0

## Lang_50
Lang_50: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang.time.FastDateFormatTest::test_changeDefault_Locale_DateTimeInstance

## Lang_51
Lang_51: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 0

## Lang_52
Lang_52: Running ant (compile.tests)................................................ FAIL
Executed command:  cd /ymy/test/Lang_52_buggy && /opt/defects4j/major/bin/ant -f /opt/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/opt/defects4j -Dd4j.dir.projects=/opt/defects4j/framework/projects -Dbasedir=/ymy/test/Lang_52_buggy  compile.tests 2>&1
Buildfile: /opt/defects4j/framework/projects/defects4j.build.xml

init:
     [echo] -------- commons-lang 2.4-SNAPSHOT --------

prepare:
    [mkdir] Created dir: /ymy/test/Lang_52_buggy/target
    [mkdir] Created dir: /ymy/test/Lang_52_buggy/target/classes
    [mkdir] Created dir: /ymy/test/Lang_52_buggy/target/conf
    [mkdir] Created dir: /ymy/test/Lang_52_buggy/target/tests

static:
     [copy] Copying 1 file to /ymy/test/Lang_52_buggy/target/conf

compile:
    [javac] /ymy/test/Lang_52_buggy/build.xml:65: warning: 'includeantruntime' was not set, defaulting to build.sysclasspath=last; set to false for repeatable builds
    [javac] Compiling 77 source files to /ymy/test/Lang_52_buggy/target/classes
    [javac] warning: [options] bootstrap class path not set in conjunction with -source 6
    [javac] warning: [options] source value 6 is obsolete and will be removed in a future release
    [javac] warning: [options] target value 1.6 is obsolete and will be removed in a future release
    [javac] warning: [options] To suppress warnings about obsolete options, use -Xlint:-options.
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:225: error: illegal start of type
    [javac]                 switch (ch) {
    [javac]                 ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:225: error: <identifier> expected
    [javac]                 switch (ch) {
    [javac]                           ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:226: error: orphaned case
    [javac]                     case '\'':
    [javac]                     ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:245: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:257: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:268: error: class, interface, or enum expected
    [javac]     public static String unescapeJava(String str) {
    [javac]                   ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:271: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:274: error: class, interface, or enum expected
    [javac]             unescapeJava(writer, str);
    [javac]             ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:275: error: class, interface, or enum expected
    [javac]             return writer.toString();
    [javac]             ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:276: error: class, interface, or enum expected
    [javac]         } catch (IOException ioe) {
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:279: error: class, interface, or enum expected
    [javac]             return null;
    [javac]             ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:280: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:298: error: class, interface, or enum expected
    [javac]     public static void unescapeJava(Writer out, String str) throws IOException {
    [javac]                   ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:301: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:304: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:306: error: class, interface, or enum expected
    [javac]         StringBuffer unicode = new StringBuffer(4);
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:307: error: class, interface, or enum expected
    [javac]         boolean hadSlash = false;
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:308: error: class, interface, or enum expected
    [javac]         boolean inUnicode = false;
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:309: error: class, interface, or enum expected
    [javac]         for (int i = 0; i < sz; i++) {
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:309: error: class, interface, or enum expected
    [javac]         for (int i = 0; i < sz; i++) {
    [javac]                         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:309: error: class, interface, or enum expected
    [javac]         for (int i = 0; i < sz; i++) {
    [javac]                                 ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:311: error: class, interface, or enum expected
    [javac]             if (inUnicode) {
    [javac]             ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:315: error: class, interface, or enum expected
    [javac]                 if (unicode.length() == 4) {
    [javac]                 ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:320: error: class, interface, or enum expected
    [javac]                         out.write((char) value);
    [javac]                         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:321: error: class, interface, or enum expected
    [javac]                         unicode.setLength(0);
    [javac]                         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:322: error: class, interface, or enum expected
    [javac]                         inUnicode = false;
    [javac]                         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:323: error: class, interface, or enum expected
    [javac]                         hadSlash = false;
    [javac]                         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:324: error: class, interface, or enum expected
    [javac]                     } catch (NumberFormatException nfe) {
    [javac]                     ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:326: error: class, interface, or enum expected
    [javac]                     }
    [javac]                     ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:329: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:333: error: class, interface, or enum expected
    [javac]                 switch (ch) {
    [javac]                 ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:336: error: class, interface, or enum expected
    [javac]                         break;
    [javac]                         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:337: error: class, interface, or enum expected
    [javac]                     case '\'':
    [javac]                     ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:339: error: class, interface, or enum expected
    [javac]                         break;
    [javac]                         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:340: error: class, interface, or enum expected
    [javac]                     case '\"':
    [javac]                     ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:342: error: class, interface, or enum expected
    [javac]                         break;
    [javac]                         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:343: error: class, interface, or enum expected
    [javac]                     case 'r':
    [javac]                     ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:345: error: class, interface, or enum expected
    [javac]                         break;
    [javac]                         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:346: error: class, interface, or enum expected
    [javac]                     case 'f':
    [javac]                     ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:348: error: class, interface, or enum expected
    [javac]                         break;
    [javac]                         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:349: error: class, interface, or enum expected
    [javac]                     case 't':
    [javac]                     ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:351: error: class, interface, or enum expected
    [javac]                         break;
    [javac]                         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:352: error: class, interface, or enum expected
    [javac]                     case 'n':
    [javac]                     ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:354: error: class, interface, or enum expected
    [javac]                         break;
    [javac]                         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:355: error: class, interface, or enum expected
    [javac]                     case 'b':
    [javac]                     ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:357: error: class, interface, or enum expected
    [javac]                         break;
    [javac]                         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:358: error: class, interface, or enum expected
    [javac]                     case 'u':
    [javac]                     ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:362: error: class, interface, or enum expected
    [javac]                             break;
    [javac]                             ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:363: error: class, interface, or enum expected
    [javac]                         }
    [javac]                         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:366: error: class, interface, or enum expected
    [javac]                         break;
    [javac]                         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:367: error: class, interface, or enum expected
    [javac]                 }
    [javac]                 ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:369: error: class, interface, or enum expected
    [javac]             } else if (ch == '\\') {
    [javac]             ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:371: error: class, interface, or enum expected
    [javac]                 continue;
    [javac]                 ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:372: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:374: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:379: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:393: error: class, interface, or enum expected
    [javac]     public static String unescapeJavaScript(String str) {
    [javac]                   ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:395: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:413: error: class, interface, or enum expected
    [javac]     public static void unescapeJavaScript(Writer out, String str) throws IOException {
    [javac]                   ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:415: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:445: error: class, interface, or enum expected
    [javac]     public static String escapeHtml(String str) {
    [javac]                   ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:448: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:451: error: class, interface, or enum expected
    [javac]             escapeHtml(writer, str);
    [javac]             ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:452: error: class, interface, or enum expected
    [javac]             return writer.toString();
    [javac]             ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:453: error: class, interface, or enum expected
    [javac]         } catch (IOException e) {
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:457: error: class, interface, or enum expected
    [javac]             return null;
    [javac]             ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:458: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:490: error: class, interface, or enum expected
    [javac]     public static void escapeHtml(Writer writer, String string) throws IOException {
    [javac]                   ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:493: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:496: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:498: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:517: error: class, interface, or enum expected
    [javac]     public static String unescapeHtml(String str) {
    [javac]                   ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:520: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:523: error: class, interface, or enum expected
    [javac]             unescapeHtml(writer, str);
    [javac]             ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:524: error: class, interface, or enum expected
    [javac]             return writer.toString();
    [javac]             ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:525: error: class, interface, or enum expected
    [javac]         } catch (IOException e) {
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:529: error: class, interface, or enum expected
    [javac]             return null;
    [javac]             ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:530: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:551: error: class, interface, or enum expected
    [javac]     public static void unescapeHtml(Writer writer, String string) throws IOException {
    [javac]                   ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:554: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:557: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:559: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:581: error: class, interface, or enum expected
    [javac]     public static void escapeXml(Writer writer, String str) throws IOException {
    [javac]                   ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:584: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:587: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:589: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:608: error: class, interface, or enum expected
    [javac]     public static String escapeXml(String str) {
    [javac]                   ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:611: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:613: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:633: error: class, interface, or enum expected
    [javac]     public static void unescapeXml(Writer writer, String str) throws IOException {
    [javac]                   ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:636: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:639: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:641: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:658: error: class, interface, or enum expected
    [javac]     public static String unescapeXml(String str) {
    [javac]                   ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:661: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:663: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:684: error: class, interface, or enum expected
    [javac]     public static String escapeSql(String str) {
    [javac]                   ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:687: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_52_buggy/src/java/org/apache/commons/lang/StringEscapeUtils.java:689: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] 99 errors
    [javac] 4 warnings

BUILD FAILED
/ymy/test/Lang_52_buggy/build.xml:65: Compile failed; see the compiler error output for details.

Total time: 0 seconds
Cannot compile test suite! at /opt/defects4j/framework/bin/d4j/d4j-test line 134.
Compilation failed in require at /opt/defects4j/framework/bin/defects4j line 195.

## Lang_53
Lang_53: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 0

## Lang_54
Lang_54: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang.LocaleUtilsTest::testToLocale_1Part

## Lang_56
Lang_56: Running ant (compile.tests)................................................ FAIL
Executed command:  cd /ymy/test/Lang_56_buggy && /opt/defects4j/major/bin/ant -f /opt/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/opt/defects4j -Dd4j.dir.projects=/opt/defects4j/framework/projects -Dbasedir=/ymy/test/Lang_56_buggy  compile.tests 2>&1
Buildfile: /opt/defects4j/framework/projects/defects4j.build.xml

init:
     [echo] -------- commons-lang 2.3-SNAPSHOT --------

prepare:
    [mkdir] Created dir: /ymy/test/Lang_56_buggy/target
    [mkdir] Created dir: /ymy/test/Lang_56_buggy/target/classes
    [mkdir] Created dir: /ymy/test/Lang_56_buggy/target/conf
    [mkdir] Created dir: /ymy/test/Lang_56_buggy/target/tests

static:
     [copy] Copying 1 file to /ymy/test/Lang_56_buggy/target/conf

compile:
    [javac] /ymy/test/Lang_56_buggy/build.xml:65: warning: 'includeantruntime' was not set, defaulting to build.sysclasspath=last; set to false for repeatable builds
    [javac] Compiling 77 source files to /ymy/test/Lang_56_buggy/target/classes
    [javac] warning: [options] bootstrap class path not set in conjunction with -source 6
    [javac] warning: [options] source value 6 is obsolete and will be removed in a future release
    [javac] warning: [options] target value 1.6 is obsolete and will be removed in a future release
    [javac] warning: [options] To suppress warnings about obsolete options, use -Xlint:-options.
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:2334: warning: [deprecation] Character(char) in Character has been deprecated
    [javac]             result[i] = new Character(array[i]);
    [javac]                         ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:2402: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]             result[i] = new Long(array[i]);
    [javac]                         ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:2470: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]             result[i] = new Integer(array[i]);
    [javac]                         ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:2538: warning: [deprecation] Short(short) in Short has been deprecated
    [javac]             result[i] = new Short(array[i]);
    [javac]                         ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:2606: warning: [deprecation] Byte(byte) in Byte has been deprecated
    [javac]             result[i] = new Byte(array[i]);
    [javac]                         ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:2674: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]             result[i] = new Double(array[i]);
    [javac]                         ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:2742: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]             result[i] = new Float(array[i]);
    [javac]                         ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:3574: warning: [deprecation] Character(char) in Character has been deprecated
    [javac]         return (char[]) add( array, index, new Character(element), Character.TYPE );
    [javac]                                            ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:3605: warning: [deprecation] Byte(byte) in Byte has been deprecated
    [javac]         return (byte[]) add( array, index, new Byte(element), Byte.TYPE );
    [javac]                                            ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:3636: warning: [deprecation] Short(short) in Short has been deprecated
    [javac]         return (short[]) add( array, index, new Short(element), Short.TYPE );
    [javac]                                             ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:3667: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]         return (int[]) add( array, index, new Integer(element), Integer.TYPE );
    [javac]                                           ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:3698: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]         return (long[]) add( array, index, new Long(element), Long.TYPE );
    [javac]                                            ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:3729: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]         return (float[]) add( array, index, new Float(element), Float.TYPE );
    [javac]                                             ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/ArrayUtils.java:3760: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]         return (double[]) add( array, index, new Double(element), Double.TYPE );
    [javac]                                              ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/CharUtils.java:75: warning: [deprecation] Character(char) in Character has been deprecated
    [javac]             CHAR_ARRAY[i] = new Character((char) i);
    [javac]                             ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/CharUtils.java:109: warning: [deprecation] Character(char) in Character has been deprecated
    [javac]         return new Character(ch);
    [javac]                ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/Entities.java:427: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]             mapNameToValue.put(name, new Integer(value));
    [javac]                                      ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/Entities.java:459: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]             mapNameToValue.put(name, new Integer(value));
    [javac]                                      ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/Entities.java:460: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]             mapValueToName.put(new Integer(value), name);
    [javac]                                ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/Entities.java:467: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]             return (String) mapValueToName.get(new Integer(value));
    [javac]                                                ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/builder/HashCodeBuilder.java:521: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]         return new Integer(System.identityHashCode(value));
    [javac]                ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/enums/Enum.java:652: warning: non-varargs call of varargs method with inexact argument type for last parameter;
    [javac]             Method mth = other.getClass().getMethod("getName", null);
    [javac]                                                                ^
    [javac]   cast to Class<?> for a varargs call
    [javac]   cast to Class<?>[] for a non-varargs call and to suppress this warning
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/enums/Enum.java:653: warning: non-varargs call of varargs method with inexact argument type for last parameter;
    [javac]             String name = (String) mth.invoke(other, null);
    [javac]                                                      ^
    [javac]   cast to Object for a varargs call
    [javac]   cast to Object[] for a non-varargs call and to suppress this warning
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/enums/ValuedEnum.java:209: warning: non-varargs call of varargs method with inexact argument type for last parameter;
    [javac]             Method mth = other.getClass().getMethod("getValue", null);
    [javac]                                                                 ^
    [javac]   cast to Class<?> for a varargs call
    [javac]   cast to Class<?>[] for a non-varargs call and to suppress this warning
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/enums/ValuedEnum.java:210: warning: non-varargs call of varargs method with inexact argument type for last parameter;
    [javac]             Integer value = (Integer) mth.invoke(other, null);
    [javac]                                                         ^
    [javac]   cast to Object for a varargs call
    [javac]   cast to Object[] for a non-varargs call and to suppress this warning
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/exception/ExceptionUtils.java:90: warning: non-varargs call of varargs method with inexact argument type for last parameter;
    [javac]             causeMethod = Throwable.class.getMethod("getCause", null);
    [javac]                                                                 ^
    [javac]   cast to Class<?> for a varargs call
    [javac]   cast to Class<?>[] for a non-varargs call and to suppress this warning
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/exception/ExceptionUtils.java:371: warning: non-varargs call of varargs method with inexact argument type for last parameter;
    [javac]             method = throwable.getClass().getMethod(methodName, null);
    [javac]                                                                 ^
    [javac]   cast to Class<?> for a varargs call
    [javac]   cast to Class<?>[] for a non-varargs call and to suppress this warning
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/exception/ExceptionUtils.java:461: warning: non-varargs call of varargs method with inexact argument type for last parameter;
    [javac]                 Method method = cls.getMethod(CAUSE_METHOD_NAMES[i], null);
    [javac]                                                                      ^
    [javac]   cast to Class for a varargs call
    [javac]   cast to Class[] for a non-varargs call and to suppress this warning
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/DoubleRange.java:182: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]             minObject = new Double(min);            
    [javac]                         ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/DoubleRange.java:236: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]             maxObject = new Double(max);            
    [javac]                         ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/FloatRange.java:182: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]             minObject = new Float(min);            
    [javac]                         ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/FloatRange.java:234: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]             maxObject = new Float(max);            
    [javac]                         ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/IntRange.java:165: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]             minObject = new Integer(min);            
    [javac]                         ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/IntRange.java:213: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]             maxObject = new Integer(max);            
    [javac]                         ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/LongRange.java:166: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]             minObject = new Long(min);            
    [javac]                         ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/LongRange.java:220: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]             maxObject = new Long(max);            
    [javac]                         ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:41: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]     public static final Long LONG_ZERO = new Long(0L);
    [javac]                                          ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:43: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]     public static final Long LONG_ONE = new Long(1L);
    [javac]                                         ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:45: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]     public static final Long LONG_MINUS_ONE = new Long(-1L);
    [javac]                                               ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:47: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]     public static final Integer INTEGER_ZERO = new Integer(0);
    [javac]                                                ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:49: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]     public static final Integer INTEGER_ONE = new Integer(1);
    [javac]                                               ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:51: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]     public static final Integer INTEGER_MINUS_ONE = new Integer(-1);
    [javac]                                                     ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:53: warning: [deprecation] Short(short) in Short has been deprecated
    [javac]     public static final Short SHORT_ZERO = new Short((short) 0);
    [javac]                                            ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:55: warning: [deprecation] Short(short) in Short has been deprecated
    [javac]     public static final Short SHORT_ONE = new Short((short) 1);
    [javac]                                           ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:57: warning: [deprecation] Short(short) in Short has been deprecated
    [javac]     public static final Short SHORT_MINUS_ONE = new Short((short) -1);
    [javac]                                                 ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:59: warning: [deprecation] Byte(byte) in Byte has been deprecated
    [javac]     public static final Byte BYTE_ZERO = new Byte((byte) 0);
    [javac]                                          ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:61: warning: [deprecation] Byte(byte) in Byte has been deprecated
    [javac]     public static final Byte BYTE_ONE = new Byte((byte) 1);
    [javac]                                         ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:63: warning: [deprecation] Byte(byte) in Byte has been deprecated
    [javac]     public static final Byte BYTE_MINUS_ONE = new Byte((byte) -1);
    [javac]                                               ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:65: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]     public static final Double DOUBLE_ZERO = new Double(0.0d);
    [javac]                                              ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:67: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]     public static final Double DOUBLE_ONE = new Double(1.0d);
    [javac]                                             ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:69: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]     public static final Double DOUBLE_MINUS_ONE = new Double(-1.0d);
    [javac]                                                   ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:71: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]     public static final Float FLOAT_ZERO = new Float(0.0f);
    [javac]                                            ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:73: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]     public static final Float FLOAT_ONE = new Float(1.0f);
    [javac]                                           ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/math/NumberUtils.java:75: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]     public static final Float FLOAT_MINUS_ONE = new Float(-1.0f);
    [javac]                                                 ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/mutable/MutableBoolean.java:124: warning: [deprecation] Boolean(boolean) in Boolean has been deprecated
    [javac]         return new Boolean(this.value);
    [javac]                ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/mutable/MutableByte.java:76: warning: [deprecation] Byte(byte) in Byte has been deprecated
    [javac]         return new Byte(this.value);
    [javac]                ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/mutable/MutableByte.java:157: warning: [deprecation] Byte(byte) in Byte has been deprecated
    [javac]         return new Byte(byteValue());
    [javac]                ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/mutable/MutableDouble.java:78: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]         return new Double(this.value);
    [javac]                ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/mutable/MutableDouble.java:168: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]         return new Double(doubleValue());
    [javac]                ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/mutable/MutableFloat.java:78: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]         return new Float(this.value);
    [javac]                ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/mutable/MutableFloat.java:240: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]         return new Float(floatValue());
    [javac]                ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/mutable/MutableInt.java:76: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]         return new Integer(this.value);
    [javac]                ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/mutable/MutableInt.java:220: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]         return new Integer(intValue());
    [javac]                ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/mutable/MutableLong.java:76: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]         return new Long(this.value);
    [javac]                ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/mutable/MutableLong.java:220: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]         return new Long(longValue());
    [javac]                ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/mutable/MutableShort.java:76: warning: [deprecation] Short(short) in Short has been deprecated
    [javac]         return new Short(this.value);
    [javac]                ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/mutable/MutableShort.java:229: warning: [deprecation] Short(short) in Short has been deprecated
    [javac]         return new Short(shortValue());
    [javac]                ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/oldenum/Enum.java:604: warning: non-varargs call of varargs method with inexact argument type for last parameter;
    [javac]             Method mth = other.getClass().getMethod("getName", null);
    [javac]                                                                ^
    [javac]   cast to Class<?> for a varargs call
    [javac]   cast to Class<?>[] for a non-varargs call and to suppress this warning
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/oldenum/Enum.java:605: warning: non-varargs call of varargs method with inexact argument type for last parameter;
    [javac]             String name = (String) mth.invoke(other, null);
    [javac]                                                      ^
    [javac]   cast to Object for a varargs call
    [javac]   cast to Object[] for a non-varargs call and to suppress this warning
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/time/FastDateFormat.java:281: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]         Object key = new Integer(style);
    [javac]                      ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/time/FastDateFormat.java:367: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]         Object key = new Integer(style);
    [javac]                      ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/time/FastDateFormat.java:461: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]         Object key = new Pair(new Integer(dateStyle), new Integer(timeStyle));
    [javac]                               ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/time/FastDateFormat.java:461: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]         Object key = new Pair(new Integer(dateStyle), new Integer(timeStyle));
    [javac]                                                       ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/time/FastDateFormat.java:1061: error: CharacterLiteral is not abstract and does not override abstract method estimateLength() in Rule
    [javac]     private static class CharacterLiteral implements Rule {
    [javac]                    ^
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/time/FastDateFormat.java:1078: error: cannot find symbol
    [javac]     return "[" + mObj1 + ':' + mObj2 + ']';
    [javac]                  ^
    [javac]   symbol:   variable mObj1
    [javac]   location: class CharacterLiteral
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/time/FastDateFormat.java:1078: error: cannot find symbol
    [javac]     return "[" + mObj1 + ':' + mObj2 + ']';
    [javac]                                ^
    [javac]   symbol:   variable mObj2
    [javac]   location: class CharacterLiteral
    [javac] Note: Some input files use unchecked or unsafe operations.
    [javac] Note: Recompile with -Xlint:unchecked for details.
    [javac] 3 errors
    [javac] 77 warnings

BUILD FAILED
/ymy/test/Lang_56_buggy/build.xml:65: Compile failed; see the compiler error output for details.

Total time: 1 second
Cannot compile test suite! at /opt/defects4j/framework/bin/d4j/d4j-test line 134.
Compilation failed in require at /opt/defects4j/framework/bin/defects4j line 195.

## Lang_58
Lang_58: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang.math.NumberUtilsTest::testLang300

## Lang_59
Lang_59: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 0

## Lang_60
Lang_60: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang.text.StrBuilderTest::testLang295

## Lang_61
Lang_61: Running ant (compile.tests)................................................ FAIL
Executed command:  cd /ymy/test/Lang_61_buggy && /opt/defects4j/major/bin/ant -f /opt/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/opt/defects4j -Dd4j.dir.projects=/opt/defects4j/framework/projects -Dbasedir=/ymy/test/Lang_61_buggy  compile.tests 2>&1
Buildfile: /opt/defects4j/framework/projects/defects4j.build.xml

init:
     [echo] -------- commons-lang 2.3-SNAPSHOT --------

prepare:
    [mkdir] Created dir: /ymy/test/Lang_61_buggy/target
    [mkdir] Created dir: /ymy/test/Lang_61_buggy/target/classes
    [mkdir] Created dir: /ymy/test/Lang_61_buggy/target/conf
    [mkdir] Created dir: /ymy/test/Lang_61_buggy/target/tests

static:
     [copy] Copying 1 file to /ymy/test/Lang_61_buggy/target/conf

compile:
    [javac] /ymy/test/Lang_61_buggy/build.xml:65: warning: 'includeantruntime' was not set, defaulting to build.sysclasspath=last; set to false for repeatable builds
    [javac] Compiling 77 source files to /ymy/test/Lang_61_buggy/target/classes
    [javac] warning: [options] bootstrap class path not set in conjunction with -source 6
    [javac] warning: [options] source value 6 is obsolete and will be removed in a future release
    [javac] warning: [options] target value 1.6 is obsolete and will be removed in a future release
    [javac] warning: [options] To suppress warnings about obsolete options, use -Xlint:-options.
    [javac] /ymy/test/Lang_61_buggy/src/java/org/apache/commons/lang/text/StrBuilder.java:1745: error: illegal start of type
    [javac]      */
    [javac]      ^
    [javac] 1 error
    [javac] 4 warnings

BUILD FAILED
/ymy/test/Lang_61_buggy/build.xml:65: Compile failed; see the compiler error output for details.

Total time: 0 seconds
Cannot compile test suite! at /opt/defects4j/framework/bin/d4j/d4j-test line 134.
Compilation failed in require at /opt/defects4j/framework/bin/defects4j line 195.

## Lang_62
Lang_62: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang.EntitiesTest::testNumberOverflow

## Lang_63
Lang_63: Running ant (compile.tests)................................................ FAIL
Executed command:  cd /ymy/test/Lang_63_buggy && /opt/defects4j/major/bin/ant -f /opt/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/opt/defects4j -Dd4j.dir.projects=/opt/defects4j/framework/projects -Dbasedir=/ymy/test/Lang_63_buggy  compile.tests 2>&1
Buildfile: /opt/defects4j/framework/projects/defects4j.build.xml

init:
     [echo] -------- commons-lang 2.3-SNAPSHOT --------

prepare:
    [mkdir] Created dir: /ymy/test/Lang_63_buggy/target
    [mkdir] Created dir: /ymy/test/Lang_63_buggy/target/classes
    [mkdir] Created dir: /ymy/test/Lang_63_buggy/target/conf
    [mkdir] Created dir: /ymy/test/Lang_63_buggy/target/tests

static:
     [copy] Copying 1 file to /ymy/test/Lang_63_buggy/target/conf

compile:
    [javac] /ymy/test/Lang_63_buggy/build.xml:65: warning: 'includeantruntime' was not set, defaulting to build.sysclasspath=last; set to false for repeatable builds
    [javac] Compiling 77 source files to /ymy/test/Lang_63_buggy/target/classes
    [javac] warning: [options] bootstrap class path not set in conjunction with -source 6
    [javac] warning: [options] source value 6 is obsolete and will be removed in a future release
    [javac] warning: [options] target value 1.6 is obsolete and will be removed in a future release
    [javac] warning: [options] To suppress warnings about obsolete options, use -Xlint:-options.
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:200: error: illegal start of type
    [javac]      * <p>Formats the time gap as a string.</p>
    [javac]      ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:200: error: '(' expected
    [javac]      * <p>Formats the time gap as a string.</p>
    [javac]                       ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:200: error: ';' expected
    [javac]      * <p>Formats the time gap as a string.</p>
    [javac]                               ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:200: error: ';' expected
    [javac]      * <p>Formats the time gap as a string.</p>
    [javac]                                    ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:200: error: illegal start of type
    [javac]      * <p>Formats the time gap as a string.</p>
    [javac]                                            ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:200: error: illegal start of type
    [javac]      * <p>Formats the time gap as a string.</p>
    [javac]                                             ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:200: error: <identifier> expected
    [javac]      * <p>Formats the time gap as a string.</p>
    [javac]                                               ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:202: error: '(' expected
    [javac]      * <p>The format used is the ISO8601 period format.</p>
    [javac]                      ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:202: error: ';' expected
    [javac]      * <p>The format used is the ISO8601 period format.</p>
    [javac]                             ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:202: error: ';' expected
    [javac]      * <p>The format used is the ISO8601 period format.</p>
    [javac]                                         ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:202: error: ';' expected
    [javac]      * <p>The format used is the ISO8601 period format.</p>
    [javac]                                                       ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:202: error: <identifier> expected
    [javac]      * <p>The format used is the ISO8601 period format.</p>
    [javac]                                                         ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:202: error: <identifier> expected
    [javac]      * <p>The format used is the ISO8601 period format.</p>
    [javac]                                                           ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:204: error: ';' expected
    [javac]      * @param startMillis  the start of the duration to format
    [javac]                               ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:204: error: ';' expected
    [javac]      * @param startMillis  the start of the duration to format
    [javac]                                        ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:204: error: ';' expected
    [javac]      * @param startMillis  the start of the duration to format
    [javac]                                                     ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:204: error: ';' expected
    [javac]      * @param startMillis  the start of the duration to format
    [javac]                                                               ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:205: error: ';' expected
    [javac]      * @param endMillis  the end of the duration to format
    [javac]                             ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:205: error: ';' expected
    [javac]      * @param endMillis  the end of the duration to format
    [javac]                                    ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:205: error: ';' expected
    [javac]      * @param endMillis  the end of the duration to format
    [javac]                                                 ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:205: error: ';' expected
    [javac]      * @param endMillis  the end of the duration to format
    [javac]                                                           ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:206: error: <identifier> expected
    [javac]      * @return the time as a String
    [javac]         ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:206: error: ';' expected
    [javac]      * @return the time as a String
    [javac]                        ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:206: error: ';' expected
    [javac]      * @return the time as a String
    [javac]                             ^
    [javac] /ymy/test/Lang_63_buggy/src/java/org/apache/commons/lang/time/DurationFormatUtils.java:206: error: <identifier> expected
    [javac]      * @return the time as a String
    [javac]                                    ^
    [javac] 25 errors
    [javac] 4 warnings

BUILD FAILED
/ymy/test/Lang_63_buggy/build.xml:65: Compile failed; see the compiler error output for details.

Total time: 1 second
Cannot compile test suite! at /opt/defects4j/framework/bin/d4j/d4j-test line 134.
Compilation failed in require at /opt/defects4j/framework/bin/defects4j line 195.

## Lang_64
Lang_64: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 0

## Lang_65
Lang_65: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 3
  - org.apache.commons.lang.time.DateUtilsTest::testRound
  - org.apache.commons.lang.time.DateUtilsTest::testTruncate
  - org.apache.commons.lang.time.DateUtilsTest::testTruncateLang59

