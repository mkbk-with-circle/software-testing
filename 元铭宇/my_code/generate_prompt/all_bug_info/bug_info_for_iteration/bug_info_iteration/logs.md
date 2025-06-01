## Lang_1
Lang_1: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang3.math.NumberUtilsTest::TestLang747

## Lang_3
Lang_3: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang3.math.NumberUtilsTest::testStringCreateNumberEnsureNoPrecisionLoss

## Lang_4
Lang_4: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang3.text.translate.LookupTranslatorTest::testLang882

## Lang_6
Lang_6: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 2
  - org.apache.commons.lang3.StringEscapeUtilsTest::testEscapeXmlSupplementaryCharacters
  - org.apache.commons.lang3.text.translate.NumericEntityEscaperTest::testSupplementary

## Lang_8
Lang_8: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 2
  - org.apache.commons.lang3.time.FastDateFormat_PrinterTest::testCalendarTimezoneRespected
  - org.apache.commons.lang3.time.FastDatePrinterTest::testCalendarTimezoneRespected

## Lang_10
Lang_10: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 2
  - org.apache.commons.lang3.time.FastDateFormat_ParserTest::testLANG_831
  - org.apache.commons.lang3.time.FastDateParserTest::testLANG_831

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
    [javac] /ymy/test/Lang_13_buggy/src/main/java/org/apache/commons/lang3/SerializationUtils.java:230: error: strings in switch are not supported in -source 6
    [javac]                         switch(desc.getName()) {
    [javac]                               ^
    [javac]   (use -source 7 or higher to enable strings in switch)
    [javac] /ymy/test/Lang_13_buggy/src/main/java/org/apache/commons/lang3/reflect/FieldUtils.java:305: warning: [deprecation] isAccessible() in AccessibleObject has been deprecated
    [javac]         if (forceAccess && !field.isAccessible()) {
    [javac]                                  ^
    [javac] /ymy/test/Lang_13_buggy/src/main/java/org/apache/commons/lang3/reflect/FieldUtils.java:514: warning: [deprecation] isAccessible() in AccessibleObject has been deprecated
    [javac]         if (forceAccess && !field.isAccessible()) {
    [javac]                                  ^
    [javac] /ymy/test/Lang_13_buggy/src/main/java/org/apache/commons/lang3/reflect/MemberUtils.java:55: warning: [deprecation] isAccessible() in AccessibleObject has been deprecated
    [javac]         if (o == null || o.isAccessible()) {
    [javac]                           ^
    [javac] 1 error
    [javac] 7 warnings

BUILD FAILED
/ymy/test/Lang_13_buggy/build.xml:63: Compile failed; see the compiler error output for details.

Total time: 1 second
Cannot compile test suite! at /opt/defects4j/framework/bin/d4j/d4j-test line 134.
Compilation failed in require at /opt/defects4j/framework/bin/defects4j line 195.

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
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:116: error: illegal start of type
    [javac]         if (toClass == null) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:116: error: <identifier> expected
    [javac]         if (toClass == null) {
    [javac]                    ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:121: error: illegal start of type
    [javac]         if (toClass.equals(type)) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:121: error: <identifier> expected
    [javac]         if (toClass.equals(type)) {
    [javac]                           ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:121: error: <identifier> expected
    [javac]         if (toClass.equals(type)) {
    [javac]                                ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:121: error: ';' expected
    [javac]         if (toClass.equals(type)) {
    [javac]                                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:125: error: illegal start of type
    [javac]         if (type instanceof Class<?>) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:125: error: <identifier> expected
    [javac]         if (type instanceof Class<?>) {
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:125: error: <identifier> expected
    [javac]         if (type instanceof Class<?>) {
    [javac]                                     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:130: error: illegal start of type
    [javac]         if (type instanceof ParameterizedType) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:130: error: <identifier> expected
    [javac]         if (type instanceof ParameterizedType) {
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:130: error: <identifier> expected
    [javac]         if (type instanceof ParameterizedType) {
    [javac]                                              ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:136: error: illegal start of type
    [javac]         if (type instanceof TypeVariable<?>) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:136: error: <identifier> expected
    [javac]         if (type instanceof TypeVariable<?>) {
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:136: error: <identifier> expected
    [javac]         if (type instanceof TypeVariable<?>) {
    [javac]                                            ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:150: error: illegal start of type
    [javac]         if (type instanceof GenericArrayType) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:150: error: <identifier> expected
    [javac]         if (type instanceof GenericArrayType) {
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:150: error: <identifier> expected
    [javac]         if (type instanceof GenericArrayType) {
    [javac]                                             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:159: error: illegal start of type
    [javac]         if (type instanceof WildcardType) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:159: error: <identifier> expected
    [javac]         if (type instanceof WildcardType) {
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:159: error: <identifier> expected
    [javac]         if (type instanceof WildcardType) {
    [javac]                                         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:163: error: illegal start of type
    [javac]         throw new IllegalStateException("found an unhandled type: " + type);
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:163: error: invalid method declaration; return type required
    [javac]         throw new IllegalStateException("found an unhandled type: " + type);
    [javac]                   ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:163: error: illegal start of type
    [javac]         throw new IllegalStateException("found an unhandled type: " + type);
    [javac]                                         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:175: error: class, interface, or enum expected
    [javac]     private static boolean isAssignable(Type type, ParameterizedType toParameterizedType,
    [javac]                    ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:179: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:185: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:190: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:196: error: class, interface, or enum expected
    [javac]         Map<TypeVariable<?>, Type> fromTypeVarAssigns = getTypeArguments(type, toClass, null);
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:199: error: class, interface, or enum expected
    [javac]         if (fromTypeVarAssigns == null) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:201: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:208: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:215: error: class, interface, or enum expected
    [javac]         for (Map.Entry<TypeVariable<?>, Type> entry : toTypeVarAssigns.entrySet()) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:217: error: class, interface, or enum expected
    [javac]             Type fromTypeArg = fromTypeVarAssigns.get(entry.getKey());
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:222: error: class, interface, or enum expected
    [javac]             if (fromTypeArg != null
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:227: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:231: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:235: error: class, interface, or enum expected
    [javac]         do {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:237: error: class, interface, or enum expected
    [javac]             if (result instanceof TypeVariable<?> && !result.equals(var)) {
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:239: error: class, interface, or enum expected
    [javac]                 continue;
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:240: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:242: error: class, interface, or enum expected
    [javac]         } while (true);
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:243: error: class, interface, or enum expected
    [javac]         return result;
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:244: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:260: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:266: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:271: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:275: error: class, interface, or enum expected
    [javac]         if (type instanceof Class<?>) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:279: error: class, interface, or enum expected
    [javac]             return cls.isArray()
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:281: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:287: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:294: error: class, interface, or enum expected
    [javac]                 }
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:298: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:306: error: class, interface, or enum expected
    [javac]                 }
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:310: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:317: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:320: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:336: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:342: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:347: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:350: error: class, interface, or enum expected
    [javac]         Type[] toLowerBounds = getImplicitLowerBounds(toWildcardType);
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:352: error: class, interface, or enum expected
    [javac]         if (type instanceof WildcardType) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:354: error: class, interface, or enum expected
    [javac]             Type[] upperBounds = getImplicitUpperBounds(wildcardType);
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:355: error: class, interface, or enum expected
    [javac]             Type[] lowerBounds = getImplicitLowerBounds(wildcardType);
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:357: error: class, interface, or enum expected
    [javac]             for (Type toBound : toUpperBounds) {
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:365: error: class, interface, or enum expected
    [javac]                 for (Type bound : upperBounds) {
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:368: error: class, interface, or enum expected
    [javac]                     }
    [javac]                     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:380: error: class, interface, or enum expected
    [javac]                 for (Type bound : lowerBounds) {
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:383: error: class, interface, or enum expected
    [javac]                     }
    [javac]                     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:388: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:396: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:405: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:409: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:425: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:431: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:436: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:444: error: class, interface, or enum expected
    [javac]             for (Type bound : bounds) {
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:447: error: class, interface, or enum expected
    [javac]                 }
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:454: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:457: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:471: error: class, interface, or enum expected
    [javac]             if (replacementType == null) {
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:474: error: class, interface, or enum expected
    [javac]             }
    [javac]             ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:477: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:480: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:493: error: class, interface, or enum expected
    [javac]     public static Map<TypeVariable<?>, Type> getTypeArguments(ParameterizedType type) {
    [javac]                   ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:495: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:529: error: class, interface, or enum expected
    [javac]     public static Map<TypeVariable<?>, Type> getTypeArguments(Type type, Class<?> toClass) {
    [javac]                   ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:531: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:545: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:549: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:554: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:563: error: class, interface, or enum expected
    [javac]                 }
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:567: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:575: error: class, interface, or enum expected
    [javac]                 }
    [javac]                 ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:579: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:583: error: class, interface, or enum expected
    [javac]     }
    [javac]     ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:599: error: class, interface, or enum expected
    [javac]         if (!isAssignable(cls, toClass)) {
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:601: error: class, interface, or enum expected
    [javac]         }
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:604: error: class, interface, or enum expected
    [javac]         Map<TypeVariable<?>, Type> typeVarAssigns;
    [javac]         ^
    [javac] /ymy/test/Lang_15_buggy/src/main/java/org/apache/commons/lang3/reflect/TypeUtils.java:606: error: class, interface, or enum expected
    [javac]         if (ownerType instanceof ParameterizedType) {
    [javac]         ^
    [javac] 100 errors
    [javac] 4 warnings

BUILD FAILED
/ymy/test/Lang_15_buggy/build.xml:62: Compile failed; see the compiler error output for details.

Total time: 0 seconds
Cannot compile test suite! at /opt/defects4j/framework/bin/d4j/d4j-test line 134.
Compilation failed in require at /opt/defects4j/framework/bin/defects4j line 195.

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
    [javac] /ymy/test/Lang_20_buggy/src/main/java/org/apache/commons/lang3/StringUtils.java:3230: error: illegal start of type
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
Lang_23: Running ant (compile.tests)................................................ FAIL
Executed command:  cd /ymy/test/Lang_23_buggy && /opt/defects4j/major/bin/ant -f /opt/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/opt/defects4j -Dd4j.dir.projects=/opt/defects4j/framework/projects -Dbasedir=/ymy/test/Lang_23_buggy  compile.tests 2>&1
Buildfile: /opt/defects4j/framework/projects/defects4j.build.xml

test-offline:

get-deps:

compile:
    [mkdir] Created dir: /ymy/test/Lang_23_buggy/target/classes
    [javac] /ymy/test/Lang_23_buggy/maven-build.xml:75: warning: 'includeantruntime' was not set, defaulting to build.sysclasspath=last; set to false for repeatable builds
    [javac] Compiling 93 source files to /ymy/test/Lang_23_buggy/target/classes
    [javac] warning: [options] bootstrap class path not set in conjunction with -source 6
    [javac] warning: [options] source value 6 is obsolete and will be removed in a future release
    [javac] warning: [options] target value 1.6 is obsolete and will be removed in a future release
    [javac] warning: [options] To suppress warnings about obsolete options, use -Xlint:-options.
    [javac] /ymy/test/Lang_23_buggy/src/main/java/org/apache/commons/lang3/text/ExtendedMessageFormat.java:498: error: method references are not supported in -source 6
    [javac]         return coll.stream().anyMatch(Objects::nonNull);
    [javac]                                                ^
    [javac]   (use -source 8 or higher to enable method references)
    [javac] 1 error
    [javac] 4 warnings

BUILD FAILED
/ymy/test/Lang_23_buggy/maven-build.xml:75: Compile failed; see the compiler error output for details.

Total time: 0 seconds
Cannot compile test suite! at /opt/defects4j/framework/bin/d4j/d4j-test line 134.
Compilation failed in require at /opt/defects4j/framework/bin/defects4j line 195.

## Lang_27
Lang_27: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 0

## Lang_30
Lang_30: Running ant (compile.tests)................................................ FAIL
Executed command:  cd /ymy/test/Lang_30_buggy && /opt/defects4j/major/bin/ant -f /opt/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/opt/defects4j -Dd4j.dir.projects=/opt/defects4j/framework/projects -Dbasedir=/ymy/test/Lang_30_buggy  compile.tests 2>&1
Buildfile: /opt/defects4j/framework/projects/defects4j.build.xml

test-offline:

get-deps:

compile:
    [mkdir] Created dir: /ymy/test/Lang_30_buggy/target/classes
    [javac] /ymy/test/Lang_30_buggy/maven-build.xml:75: warning: 'includeantruntime' was not set, defaulting to build.sysclasspath=last; set to false for repeatable builds
    [javac] Compiling 84 source files to /ymy/test/Lang_30_buggy/target/classes
    [javac] warning: [options] bootstrap class path not set in conjunction with -source 6
    [javac] warning: [options] source value 6 is obsolete and will be removed in a future release
    [javac] warning: [options] target value 1.6 is obsolete and will be removed in a future release
    [javac] warning: [options] To suppress warnings about obsolete options, use -Xlint:-options.
    [javac] /ymy/test/Lang_30_buggy/src/main/java/org/apache/commons/lang3/StringUtils.java:1360: error: ')' expected
    [javac]                 if (Character.isHighSurrogate(ch) {
    [javac]                                                  ^
    [javac] 1 error
    [javac] 4 warnings

BUILD FAILED
/ymy/test/Lang_30_buggy/maven-build.xml:75: Compile failed; see the compiler error output for details.

Total time: 0 seconds
Cannot compile test suite! at /opt/defects4j/framework/bin/d4j/d4j-test line 134.
Compilation failed in require at /opt/defects4j/framework/bin/defects4j line 195.

## Lang_32
Lang_32: Running ant (compile.tests)................................................ FAIL
Executed command:  cd /ymy/test/Lang_32_buggy && /opt/defects4j/major/bin/ant -f /opt/defects4j/framework/projects/defects4j.build.xml -Dd4j.home=/opt/defects4j -Dd4j.dir.projects=/opt/defects4j/framework/projects -Dbasedir=/ymy/test/Lang_32_buggy  compile.tests 2>&1
Buildfile: /opt/defects4j/framework/projects/defects4j.build.xml

test-offline:

get-deps:

compile:
    [mkdir] Created dir: /ymy/test/Lang_32_buggy/target/classes
    [javac] /ymy/test/Lang_32_buggy/maven-build.xml:75: warning: 'includeantruntime' was not set, defaulting to build.sysclasspath=last; set to false for repeatable builds
    [javac] Compiling 80 source files to /ymy/test/Lang_32_buggy/target/classes
    [javac] warning: [options] bootstrap class path not set in conjunction with -source 6
    [javac] warning: [options] source value 6 is obsolete and will be removed in a future release
    [javac] warning: [options] target value 1.6 is obsolete and will be removed in a future release
    [javac] warning: [options] To suppress warnings about obsolete options, use -Xlint:-options.
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/CharUtils.java:75: warning: [deprecation] Character(char) in Character has been deprecated
    [javac]             CHAR_ARRAY[i] = new Character((char) i);
    [javac]                             ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/CharUtils.java:109: warning: [deprecation] Character(char) in Character has been deprecated
    [javac]         return new Character(ch);
    [javac]                ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/Validate.java:121: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]             throw new IllegalArgumentException(String.format(message, new Double(value)));
    [javac]                                                                       ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/builder/HashCodeBuilder.java:111: error: cannot find symbol
    [javac]                 HashCodeBuilder.cleanupRegistry();
    [javac]                                ^
    [javac]   symbol:   method cleanupRegistry()
    [javac]   location: class HashCodeBuilder
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/builder/HashCodeBuilder.java:120: error: cannot find symbol
    [javac]                 HashCodeBuilder.cleanupRegistry();
    [javac]                                ^
    [javac]   symbol:   method cleanupRegistry()
    [javac]   location: class HashCodeBuilder
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/builder/HashCodeBuilder.java:128: error: cannot find symbol
    [javac]             HashCodeBuilder.cleanupRegistry();
    [javac]                            ^
    [javac]   symbol:   method cleanupRegistry()
    [javac]   location: class HashCodeBuilder
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/math/NumberUtils.java:41: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]     public static final Long LONG_ZERO = new Long(0L);
    [javac]                                          ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/math/NumberUtils.java:43: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]     public static final Long LONG_ONE = new Long(1L);
    [javac]                                         ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/math/NumberUtils.java:45: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]     public static final Long LONG_MINUS_ONE = new Long(-1L);
    [javac]                                               ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/math/NumberUtils.java:47: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]     public static final Integer INTEGER_ZERO = new Integer(0);
    [javac]                                                ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/math/NumberUtils.java:49: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]     public static final Integer INTEGER_ONE = new Integer(1);
    [javac]                                               ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/math/NumberUtils.java:51: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]     public static final Integer INTEGER_MINUS_ONE = new Integer(-1);
    [javac]                                                     ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/math/NumberUtils.java:53: warning: [deprecation] Short(short) in Short has been deprecated
    [javac]     public static final Short SHORT_ZERO = new Short((short) 0);
    [javac]                                            ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/math/NumberUtils.java:55: warning: [deprecation] Short(short) in Short has been deprecated
    [javac]     public static final Short SHORT_ONE = new Short((short) 1);
    [javac]                                           ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/math/NumberUtils.java:57: warning: [deprecation] Short(short) in Short has been deprecated
    [javac]     public static final Short SHORT_MINUS_ONE = new Short((short) -1);
    [javac]                                                 ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/math/NumberUtils.java:65: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]     public static final Double DOUBLE_ZERO = new Double(0.0d);
    [javac]                                              ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/math/NumberUtils.java:67: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]     public static final Double DOUBLE_ONE = new Double(1.0d);
    [javac]                                             ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/math/NumberUtils.java:69: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]     public static final Double DOUBLE_MINUS_ONE = new Double(-1.0d);
    [javac]                                                   ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/math/NumberUtils.java:71: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]     public static final Float FLOAT_ZERO = new Float(0.0f);
    [javac]                                            ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/math/NumberUtils.java:73: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]     public static final Float FLOAT_ONE = new Float(1.0f);
    [javac]                                           ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/math/NumberUtils.java:75: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]     public static final Float FLOAT_MINUS_ONE = new Float(-1.0f);
    [javac]                                                 ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/mutable/MutableDouble.java:85: warning: [deprecation] Double(double) in Double has been deprecated
    [javac]         return new Double(this.value);
    [javac]                ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/mutable/MutableFloat.java:85: warning: [deprecation] Float(float) in Float has been deprecated
    [javac]         return new Float(this.value);
    [javac]                ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/mutable/MutableInt.java:85: warning: [deprecation] Integer(int) in Integer has been deprecated
    [javac]         return new Integer(this.value);
    [javac]                ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/mutable/MutableLong.java:85: warning: [deprecation] Long(long) in Long has been deprecated
    [javac]         return new Long(this.value);
    [javac]                ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/mutable/MutableShort.java:85: warning: [deprecation] Short(short) in Short has been deprecated
    [javac]         return new Short(this.value);
    [javac]                ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/reflect/FieldUtils.java:311: warning: [deprecation] isAccessible() in AccessibleObject has been deprecated
    [javac]         if (forceAccess && !field.isAccessible()) {
    [javac]                                  ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/reflect/FieldUtils.java:518: warning: [deprecation] isAccessible() in AccessibleObject has been deprecated
    [javac]         if (forceAccess && !field.isAccessible()) {
    [javac]                                  ^
    [javac] /ymy/test/Lang_32_buggy/src/main/java/org/apache/commons/lang3/reflect/MemberUtils.java:58: warning: [deprecation] isAccessible() in AccessibleObject has been deprecated
    [javac]         if (o == null || o.isAccessible()) {
    [javac]                           ^
    [javac] 3 errors
    [javac] 30 warnings

BUILD FAILED
/ymy/test/Lang_32_buggy/maven-build.xml:75: Compile failed; see the compiler error output for details.

Total time: 2 seconds
Cannot compile test suite! at /opt/defects4j/framework/bin/d4j/d4j-test line 134.
Compilation failed in require at /opt/defects4j/framework/bin/defects4j line 195.

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
Failing tests: 2
  - org.apache.commons.lang3.math.NumberUtilsTest::testCreateNumber
  - org.apache.commons.lang3.math.NumberUtilsTest::testIsNumber

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

## Lang_43
Lang_43: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang.text.ExtendedMessageFormatTest::testEscapedQuote_LANG_477

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
    [javac]         return escapeJavaStyleString(str, false, true);
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

Total time: 1 second
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
Failing tests: 1
  - org.apache.commons.lang.math.FractionTest::testReduce

## Lang_50
Lang_50: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang.time.FastDateFormatTest::test_changeDefault_Locale_DateTimeInstance

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
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/time/FastDateFormat.java:1074: error: cannot find symbol
    [javac] private static class PaddedNumberField implements Serializable {
    [javac]                                                   ^
    [javac]   symbol:   class Serializable
    [javac]   location: class CharacterLiteral
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
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/time/FastDateFormat.java:1079: error: cannot find symbol
    [javac]         return "[" + mObj1 + ':' + mObj2 + ']';
    [javac]                      ^
    [javac]   symbol:   variable mObj1
    [javac]   location: class PaddedNumberField
    [javac] /ymy/test/Lang_56_buggy/src/java/org/apache/commons/lang/time/FastDateFormat.java:1079: error: cannot find symbol
    [javac]         return "[" + mObj1 + ':' + mObj2 + ']';
    [javac]                                    ^
    [javac]   symbol:   variable mObj2
    [javac]   location: class PaddedNumberField
    [javac] Note: Some input files use unchecked or unsafe operations.
    [javac] Note: Recompile with -Xlint:unchecked for details.
    [javac] 4 errors
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

## Lang_60
Lang_60: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang.text.StrBuilderTest::testLang295

## Lang_62
Lang_62: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 1
  - org.apache.commons.lang.EntitiesTest::testNumberOverflow

## Lang_65
Lang_65: Running ant (compile.tests)................................................ OK
Running ant (run.dev.tests)................................................ OK
Failing tests: 3
  - org.apache.commons.lang.time.DateUtilsTest::testRound
  - org.apache.commons.lang.time.DateUtilsTest::testTruncate
  - org.apache.commons.lang.time.DateUtilsTest::testTruncateLang59

