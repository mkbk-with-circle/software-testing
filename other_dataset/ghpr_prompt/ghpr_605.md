## Buggy code
```java
/*
 *
 */
package com.sun.jna.platform.win32;

import java.util.List;

import com.sun.jna.IntegerType;
import com.sun.jna.NativeLong;
import com.sun.jna.Pointer;
import com.sun.jna.Structure;
import com.sun.jna.Union;
import com.sun.jna.platform.win32.BaseTSD.ULONG_PTR;
import com.sun.jna.platform.win32.Guid.GUID;
import com.sun.jna.platform.win32.Variant.VARIANT;
import com.sun.jna.platform.win32.Variant.VariantArg;
import com.sun.jna.platform.win32.WTypes.BSTR;
import com.sun.jna.platform.win32.WTypes.LPOLESTR;
import com.sun.jna.platform.win32.WTypes.VARTYPE;
import com.sun.jna.platform.win32.WinDef.BYTE;
import com.sun.jna.platform.win32.WinDef.DWORD;
import com.sun.jna.platform.win32.WinDef.DWORDByReference;
import com.sun.jna.platform.win32.WinDef.LCID;
import com.sun.jna.platform.win32.WinDef.LONG;
import com.sun.jna.platform.win32.WinDef.LONGLONG;
import com.sun.jna.platform.win32.WinDef.PVOID;
import com.sun.jna.platform.win32.WinDef.SCODE;
import com.sun.jna.platform.win32.WinDef.SHORT;
import com.sun.jna.platform.win32.WinDef.ULONG;
import com.sun.jna.platform.win32.WinDef.ULONGLONG;
import com.sun.jna.platform.win32.WinDef.USHORT;
import com.sun.jna.platform.win32.WinDef.WORD;
import com.sun.jna.platform.win32.COM.TypeComp;
import com.sun.jna.ptr.ByReference;

// TODO: Auto-generated Javadoc
/**
 * The Interface OaIdl.
 */
public interface OaIdl {

    /**
     * The Class EXCEPINFO.
     */
    public static class EXCEPINFO extends Structure {

        /**
         * The Class ByReference.
         */
        public static class ByReference extends EXCEPINFO implements
                Structure.ByReference {
        }

        public static final List<String> FIELDS = createFieldsOrder("wCode", "wReserved", "bstrSource",
                "bstrDescription", "bstrHelpFile", "dwHelpContext",
                "pvReserved", "pfnDeferredFillIn", "scode");

        /** The w code. */
        public WORD wCode;

        /** The w reserved. */
        public WORD wReserved;

        /** The bstr source. */
        public BSTR bstrSource;

        /** The bstr description. */
        public BSTR bstrDescription;

        /** The bstr help file. */
        public BSTR bstrHelpFile;

        /** The dw help context. */
        public DWORD dwHelpContext;

        /** The pv reserved. */
        public PVOID pvReserved;

        /** The pfn deferred fill in. */
        public EXCEPINFO.ByReference pfnDeferredFillIn;

        /** The scode. */
        public SCODE scode;

        /**
         * Instantiates a new excepinfo.
         */
        public EXCEPINFO() {
            super();
        }

        /**
         * Instantiates a new excepinfo.
         *
         * @param p
         *            the p
         */
        public EXCEPINFO(Pointer p) {
            super(p);
        }

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    }

    public static class VARIANT_BOOL extends IntegerType {
        private static final long serialVersionUID = 1L;
        public static final int SIZE = 2;

        public VARIANT_BOOL() {
            this(0);
        }

        public VARIANT_BOOL(long value) {
            super(2, value);
        }
    }

    public static class _VARIANT_BOOL extends VARIANT_BOOL {
        private static final long serialVersionUID = 1L;

        public _VARIANT_BOOL() {
            this(0);
        }

        public _VARIANT_BOOL(long value) {
            super(value);
        }
    }

    public static class VARIANT_BOOLByReference extends ByReference {
        public VARIANT_BOOLByReference() {
            this(new VARIANT_BOOL(0));
        }

        public VARIANT_BOOLByReference(VARIANT_BOOL value) {
            super(VARIANT_BOOL.SIZE);
            setValue(value);
        }

        public void setValue(VARIANT_BOOL value) {
            getPointer().setShort(0, value.shortValue());
        }

        public VARIANT_BOOL getValue() {
            return new VARIANT_BOOL(getPointer().getShort(0));
        }
    }

    public static class _VARIANT_BOOLByReference extends ByReference {
        public _VARIANT_BOOLByReference() {
            this(new VARIANT_BOOL(0));
        }

        public _VARIANT_BOOLByReference(VARIANT_BOOL value) {
            super(VARIANT_BOOL.SIZE);
            setValue(value);
        }

        public void setValue(VARIANT_BOOL value) {
            getPointer().setShort(0, value.shortValue());
        }

        public VARIANT_BOOL getValue() {
            return new VARIANT_BOOL(getPointer().getShort(0));
        }
    }

    public static class DATE extends Structure {
        public static class ByReference extends DATE implements
                Structure.ByReference {
        }

        public static final List<String> FIELDS = createFieldsOrder("date");
        public double date;

        public DATE() {
            super();
        }

        public DATE(double date) {
            this.date = date;
        }

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    }

    /**
     * The Class DISPID.
     */
    public static class DISPID extends LONG {
        private static final long serialVersionUID = 1L;

        public DISPID() {
            this(0);
        }

        public DISPID(int value) {
            super(value);
        }
    }

    public static class DISPIDByReference extends ByReference {
        public DISPIDByReference() {
            this(new DISPID(0));
        }

        public DISPIDByReference(DISPID value) {
            super(DISPID.SIZE);
            setValue(value);
        }

        public void setValue(DISPID value) {
            getPointer().setInt(0, value.intValue());
        }

        public DISPID getValue() {
            return new DISPID(getPointer().getInt(0));
        }
    }

    public static class MEMBERID extends DISPID {
        private static final long serialVersionUID = 1L;

        public MEMBERID() {
            this(0);
        }

        public MEMBERID(int value) {
            super(value);
        }
    }

    public static class MEMBERIDByReference extends ByReference {
        public MEMBERIDByReference() {
            this(new MEMBERID(0));
        }

        public MEMBERIDByReference(MEMBERID value) {
            super(MEMBERID.SIZE);
            setValue(value);
        }

        public void setValue(MEMBERID value) {
            getPointer().setInt(0, value.intValue());
        }

        public MEMBERID getValue() {
            return new MEMBERID(getPointer().getInt(0));
        }
    }

    // The Collect property. You use this property if the method you are calling
    // through Invoke is an accessor function.
    /** The Constant DISPID_COLLECT. */
    public final static DISPID DISPID_COLLECT = new DISPID(-8);

    // The C++ constructor function for the object.
    /** The Constant DISPID_CONSTRUCTOR. */
    public final static DISPID DISPID_CONSTRUCTOR = new DISPID(-6);

    // The C++ destructor function for the object.
    /** The Constant DISPID_DESTRUCTOR. */
    public final static DISPID DISPID_DESTRUCTOR = new DISPID(-7);

    // The Evaluate method. This method is implicitly invoked when the ActiveX
    // client encloses the arguments in square brackets. For example, the
    // following two lines are equivalent:
    /** The Constant DISPID_EVALUATE. */
    public final static DISPID DISPID_EVALUATE = new DISPID(-5);

    // The _NewEnum property. This special, restricted property is required for
    // collection objects. It returns an enumerator object that supports
    // IEnumVARIANT, and should have the restricted attribute specified.
    /** The Constant DISPID_NEWENUM. */
    public final static DISPID DISPID_NEWENUM = new DISPID(-4);

    // The parameter that receives the value of an assignment in a PROPERTYPUT.
    /** The Constant DISPID_PROPERTYPUT. */
    public final static DISPID DISPID_PROPERTYPUT = new DISPID(-3);

    // The value returned by IDispatch::GetIDsOfNames to indicate that a member
    // or parameter name was not found.
    /** The Constant DISPID_UNKNOWN. */
    public final static DISPID DISPID_UNKNOWN = new DISPID(-1);

    // The default member for the object. This property or method is invoked
    // when an ActiveX client specifies the object name without a property or
    // method.
    /** The Constant DISPID_VALUE. */
    public final static DISPID DISPID_VALUE = new DISPID(0);

    public final static MEMBERID MEMBERID_NIL = new MEMBERID(
            DISPID_UNKNOWN.intValue());

    /** An array that is allocated on the stack. */
    public final static int FADF_AUTO = 0x0001;

    /** An array that is statically allocated. */
    public final static int FADF_STATIC = 0x0002;

    /** An array that is embedded in a structure. */
    public final static int FADF_EMBEDDED = 0x0004;

    /** An array that may not be resized or reallocated. */
    public final static int FADF_FIXEDSIZE = 0x0010;

    /**
     * An array that contains records. When set, there will be a pointer to the
     * IRecordInfo interface at negative offset 4 in the array descriptor.
     */
    public final static int FADF_RECORD = 0x0020;

    /**
     * An array that has an IID identifying interface. When set, there will be a
     * GUID at negative offset 16 in the safe array descriptor. Flag is set only
     * when FADF_DISPATCH or FADF_UNKNOWN is also set.
     */
    public final static int FADF_HAVEIID = 0x0040;

    /**
     * An array that has a variant type. The variant type can be retrieved with
     * SafeArrayGetVartype.
     */
    public final static int FADF_HAVEVARTYPE = 0x0080;

    /** An array of BSTRs. */
    public final static int FADF_BSTR = 0x0100;

    /** An array of IUnknown*. */
    public final static int FADF_UNKNOWN = 0x0200;

    /** An array of IDispatch*. */
    public final static int FADF_DISPATCH = 0x0400;

    /** An array of VARIANTs. */
    public final static int FADF_VARIANT = 0x0800;

    /** Bits reserved for future use. */
    public final static int FADF_RESERVED = 0xF008;

    public static class TYPEKIND extends Structure {
        public static class ByReference extends TYPEKIND implements
                Structure.ByReference {
            public ByReference() {

            }

            public ByReference(int value) {
                super(value);
            }

            public ByReference(TYPEKIND typekind) {
                super(typekind.getPointer());
                value = typekind.value;
            }
        }

        public static final List<String> FIELDS = createFieldsOrder("value");
        public int value;

        public TYPEKIND() {
            super();
        }

        public TYPEKIND(int value) {
            this.value = value;
        }

        public TYPEKIND(Pointer pointer) {
            super(pointer);
            this.read();
        }

        // / <i>native declaration : line 4</i>
        public static final int TKIND_ENUM = 0;
        // / <i>native declaration : line 5</i>
        public static final int TKIND_RECORD = TYPEKIND.TKIND_ENUM + 1;
        // / <i>native declaration : line 6</i>
        public static final int TKIND_MODULE = TYPEKIND.TKIND_RECORD + 1;
        // / <i>native declaration : line 7</i>
        public static final int TKIND_INTERFACE = TYPEKIND.TKIND_MODULE + 1;
        // / <i>native declaration : line 8</i>
        public static final int TKIND_DISPATCH = TYPEKIND.TKIND_INTERFACE + 1;
        // / <i>native declaration : line 9</i>
        public static final int TKIND_COCLASS = TYPEKIND.TKIND_DISPATCH + 1;
        // / <i>native declaration : line 10</i>
        public static final int TKIND_ALIAS = TYPEKIND.TKIND_COCLASS + 1;
        // / <i>native declaration : line 11</i>
        public static final int TKIND_UNION = TYPEKIND.TKIND_ALIAS + 1;
        // / <i>native declaration : line 12</i>
        public static final int TKIND_MAX = TYPEKIND.TKIND_UNION + 1;

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    };

    public static class DESCKIND extends Structure {
        public static class ByReference extends DESCKIND implements
                Structure.ByReference {
        }

        public static final List<String> FIELDS = createFieldsOrder("value");

        public int value;

        public DESCKIND() {
            super();
        }

        public DESCKIND(int value) {
            this.value = value;
        }

        public DESCKIND(Pointer pointer) {
            super(pointer);
            this.read();
        }

        // / <i>native declaration : line 4</i>
        public static final int DESCKIND_NONE = 0;
        // / <i>native declaration : line 5</i>
        public static final int DESCKIND_FUNCDESC = DESCKIND.DESCKIND_NONE + 1;
        // / <i>native declaration : line 6</i>
        public static final int DESCKIND_VARDESC = DESCKIND.DESCKIND_FUNCDESC + 1;
        // / <i>native declaration : line 7</i>
        public static final int DESCKIND_TYPECOMP = DESCKIND.DESCKIND_VARDESC + 1;
        // / <i>native declaration : line 8</i>
        public static final int DESCKIND_IMPLICITAPPOBJ = DESCKIND.DESCKIND_TYPECOMP + 1;
        // / <i>native declaration : line 9</i>
        public static final int DESCKIND_MAX = DESCKIND.DESCKIND_IMPLICITAPPOBJ + 1;

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    };

    public static class SAFEARRAY extends Structure {
        public static class ByReference extends SAFEARRAY implements
                Structure.ByReference {
        }

        public static final List<String> FIELDS = createFieldsOrder(
                "cDims", "fFeatures", "cbElements", "cLocks", "pvData", "rgsabound");

        public USHORT cDims;
        public USHORT fFeatures;
        public ULONG cbElements;
        public ULONG cLocks;
        public PVOID pvData;

        /** The rgsabound. */
        public SAFEARRAYBOUND[] rgsabound = { new SAFEARRAYBOUND() };

        public SAFEARRAY() {
            super();
        }

        public SAFEARRAY(Pointer pointer) {
            super(pointer);
            this.read();
        }

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    }

    public static class SAFEARRAYBOUND extends Structure {
        public static class ByReference extends SAFEARRAYBOUND implements
                Structure.ByReference {
        }

        public static final List<String> FIELDS = createFieldsOrder("cElements", "lLbound");

        public ULONG cElements;
        public LONG lLbound;

        public SAFEARRAYBOUND() {
            super();
        }

        public SAFEARRAYBOUND(Pointer pointer) {
            super(pointer);
            this.read();
        }

        public SAFEARRAYBOUND(int cElements, int lLbound) {
            this.cElements = new ULONG(cElements);
            this.lLbound = new LONG(lLbound);
            this.write();
        }

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    }

    public static class CURRENCY extends Union {

        public static class ByReference extends CURRENCY implements
                Structure.ByReference {
        };

        public _CURRENCY currency;
        public LONGLONG int64;

        public CURRENCY() {
            super();
        }

        public CURRENCY(Pointer pointer) {
            super(pointer);
            this.read();
        }

        public static class _CURRENCY extends Structure {
            public static final List<String> FIELDS = createFieldsOrder("Lo", "Hi");

            public ULONG Lo;
            public LONG Hi;

            public _CURRENCY() {
                super();
            }

            public _CURRENCY(Pointer pointer) {
                super(pointer);
                this.read();
            }

            @Override
            protected List<String> getFieldOrder() {
                return FIELDS;
            }
        }
    }

    public static class DECIMAL extends Structure {
        public static final List<String> FIELDS = createFieldsOrder("wReserved", "decimal1", "Hi32", "decimal2");

        public static class ByReference extends DECIMAL implements
                Structure.ByReference {
        };


        public static class _DECIMAL1 extends Union {

            public USHORT signscale;
            public _DECIMAL1_DECIMAL decimal1_DECIMAL;

            public _DECIMAL1() {
                this.setType("signscale");
            }

            public _DECIMAL1(Pointer pointer) {
                super(pointer);
                this.setType("signscale");
                this.read();
            }

            public static class _DECIMAL1_DECIMAL extends Structure {
                public static final List<String> FIELDS = createFieldsOrder("scale", "sign");
                public BYTE scale;
                public BYTE sign;

                public _DECIMAL1_DECIMAL() {
                    super();
                }

                public _DECIMAL1_DECIMAL(Pointer pointer) {
                    super(pointer);
                }

                @Override
                protected List<String> getFieldOrder() {
                    return FIELDS;
                }
            }
        }

        public static class _DECIMAL2 extends Union {
            public ULONGLONG Lo64;
            public _DECIMAL2_DECIMAL decimal2_DECIMAL;

            public _DECIMAL2() {
                this.setType("Lo64");
            }

            public _DECIMAL2(Pointer pointer) {
                super(pointer);
                this.setType("Lo64");
                this.read();
            }

            public static class _DECIMAL2_DECIMAL extends Structure {
                public static final List<String> FIELDS = createFieldsOrder("Lo32", "Mid32");

                public BYTE Lo32;
                public BYTE Mid32;

                public _DECIMAL2_DECIMAL() {
                    super();
                }

                public _DECIMAL2_DECIMAL(Pointer pointer) {
                    super(pointer);
                }

                @Override
                protected List<String> getFieldOrder() {
                    return FIELDS;
                }
            }
        }

        public short wReserved;
        public _DECIMAL1 decimal1;
        public NativeLong Hi32;
        public _DECIMAL2 decimal2;

        public DECIMAL() {
            super();
        }

        public DECIMAL(Pointer pointer) {
            super(pointer);
        }

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    }

    public static class SYSKIND extends Structure {
        public static class ByReference extends SYSKIND implements
                Structure.ByReference {
        }

        public static final List<String> FIELDS = createFieldsOrder("value");

        public int value;
        public SYSKIND() {
            super();
        }

        public SYSKIND(int value) {
            this.value = value;
        }

        public SYSKIND(Pointer pointer) {
            super(pointer);
            this.read();
        }

        public static final int SYS_WIN16 = 0;
        public static final int SYS_WIN32 = SYSKIND.SYS_WIN16 + 1;
        public static final int SYS_MAC = SYSKIND.SYS_WIN32 + 1;
        public static final int SYS_WIN64 = SYSKIND.SYS_MAC + 1;

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    };

    public static class LIBFLAGS extends Structure {
        public static class ByReference extends LIBFLAGS implements
                Structure.ByReference {
        }

        public static final List<String> FIELDS = createFieldsOrder("value");
        public int value;

        public LIBFLAGS() {
            super();
        }

        public LIBFLAGS(int value) {
            this.value = value;
        }

        public LIBFLAGS(Pointer pointer) {
            super(pointer);
            this.read();
        }

        public static final int LIBFLAG_FRESTRICTED = 0x1;
        public static final int LIBFLAG_FCONTROL = 0x2;
        public static final int LIBFLAG_FHIDDEN = 0x4;
        public static final int LIBFLAG_FHASDISKIMAGE = 0x8;

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    };

    public static class TLIBATTR extends Structure {
        public static class ByReference extends TLIBATTR implements
                Structure.ByReference {

            public ByReference() {
                super();
            }

            public ByReference(Pointer pointer) {
                super(pointer);
                this.read();
            }
        };

        public static final List<String> FIELDS = createFieldsOrder("guid", "lcid", "syskind",
                "wMajorVerNum", "wMinorVerNum", "wLibFlags");

        public GUID guid;
        public LCID lcid;
        public SYSKIND syskind;
        public WORD wMajorVerNum;
        public WORD wMinorVerNum;
        public WORD wLibFlags;

        public TLIBATTR() {
            super();
        }

        public TLIBATTR(Pointer pointer) {
            super(pointer);
            this.read();
        }

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    }

    public static class BINDPTR extends Union {
        public static class ByReference extends BINDPTR implements
                Structure.ByReference {
        };

        // / C type : FUNCDESC*
        public FUNCDESC lpfuncdesc;
        // / C type : VARDESC*
        public VARDESC lpvardesc;
        // / C type : ITypeComp*
        public TypeComp lptcomp;

        public BINDPTR() {
            super();
        }

        // / @param lpvardesc C type : VARDESC*
        public BINDPTR(VARDESC lpvardesc) {
            super();
            this.lpvardesc = lpvardesc;
            setType(VARDESC.class);
        }

        // / @param lptcomp C type : ITypeComp*
        public BINDPTR(TypeComp lptcomp) {
            super();
            this.lptcomp = lptcomp;
            setType(TypeComp.class);
        }

        // / @param lpfuncdesc C type : FUNCDESC*
        public BINDPTR(FUNCDESC lpfuncdesc) {
            super();
            this.lpfuncdesc = lpfuncdesc;
            setType(FUNCDESC.class);
        }
    }

    public static class FUNCDESC extends Structure {
        public static class ByReference extends FUNCDESC implements
                Structure.ByReference {
        };

        public static final List<String> FIELDS = createFieldsOrder("memid", "lprgscode",
                "lprgelemdescParam", "funckind", "invkind", "callconv",
                "cParams", "cParamsOpt", "oVft", "cScodes", "elemdescFunc",
                "wFuncFlags");

        public MEMBERID memid;
        public ScodeArg.ByReference lprgscode;
        public ElemDescArg.ByReference lprgelemdescParam;
        public FUNCKIND funckind;
        public INVOKEKIND invkind;
        public CALLCONV callconv;
        public SHORT cParams;
        public SHORT cParamsOpt;
        public SHORT oVft;
        public SHORT cScodes;
        public ELEMDESC elemdescFunc;
        public WORD wFuncFlags;

        public FUNCDESC() {
            super();
        }

        public FUNCDESC(Pointer pointer) {
            super(pointer);
            this.read();

            if (this.cParams.shortValue() > 1) {
                this.lprgelemdescParam.elemDescArg = new ELEMDESC[this.cParams
                        .shortValue()];
                this.lprgelemdescParam.read();
            }
        }

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    }

    public static class ElemDescArg extends Structure {
        public static class ByReference extends ElemDescArg implements
                Structure.ByReference {
        }

        public static final List<String> FIELDS = createFieldsOrder("elemDescArg");

        public ELEMDESC[] elemDescArg = { new ELEMDESC() };

        public ElemDescArg() {
            super();
        }

        public ElemDescArg(Pointer pointer) {
            super(pointer);
            this.read();
        }

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    }

    public static class ScodeArg extends Structure {
        public static class ByReference extends ScodeArg implements
                Structure.ByReference {
        }

        public static final List<String> FIELDS = createFieldsOrder("scodeArg");

        public SCODE[] scodeArg = { new SCODE() };

        public ScodeArg() {
            super();
        }

        public ScodeArg(Pointer pointer) {
            super(pointer);
            this.read();
        }

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    }

    public class VARDESC extends Structure {
        public static class ByReference extends VARDESC implements
                Structure.ByReference {
        };

        public static final List<String> FIELDS = createFieldsOrder("memid", "lpstrSchema", "_vardesc",
                "elemdescVar", "wVarFlags", "varkind");

        // / C type : MEMBERID
        public MEMBERID memid;
        // / C type : LPOLESTR
        public LPOLESTR lpstrSchema;
        /**
         * [switch_is][switch_type]<br>
         * C type : _VARDESC_union
         */
        public _VARDESC _vardesc;
        // / C type : ELEMDESC
        public ELEMDESC elemdescVar;
        public WORD wVarFlags;
        // / C type : VARKIND
        public VARKIND varkind;

        // / <i>native declaration : line 6</i>
        // / <i>native declaration : line 6</i>
        public static class _VARDESC extends Union {
            public static class ByReference extends _VARDESC implements
                    Structure.ByReference {
            };

            // / [case()]
            public NativeLong oInst;
            /**
             * [case()]<br>
             * C type : VARIANT*
             */
            public VARIANT.ByReference lpvarValue;

            public _VARDESC() {
                setType("lpvarValue");
                this.read();
            }

            public _VARDESC(Pointer pointer) {
                super(pointer);
                setType("lpvarValue");
                this.read();
            }

            /**
             * @param lpvarValue
             *            [case()]<br>
             *            C type : VARIANT*
             */
            public _VARDESC(VARIANT.ByReference lpvarValue) {
                this.lpvarValue = lpvarValue;
                setType("lpvarValue");
            }

            // / @param oInst [case()]
            public _VARDESC(NativeLong oInst) {
                this.oInst = oInst;
                setType("oInst");
            }
        };

        public VARDESC() {
            super();
        }

        public VARDESC(Pointer pointer) {
            super(pointer);
            this._vardesc.setType("lpvarValue");
            this.read();
        }

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    }

    public static class ELEMDESC extends Structure {
        public static class ByReference extends ELEMDESC implements
                Structure.ByReference {
        };

        public static final List<String> FIELDS = createFieldsOrder("tdesc", "_elemdesc");
        /**
         * the type of the element<br>
         * C type : TYPEDESC
         */
        public TYPEDESC tdesc;
        // / C type : DUMMYUNIONNAMEUnion
        public _ELEMDESC _elemdesc;

        // / <i>native declaration : line 4</i>
        // / <i>native declaration : line 4</i>
        public static class _ELEMDESC extends Union {
            public static class ByReference extends _ELEMDESC implements
                    Structure.ByReference {
            };

            /**
             * info for remoting the element<br>
             * C type : IDLDESC
             */
            public IDLDESC idldesc;
            /**
             * info about the parameter<br>
             * C type : PARAMDESC
             */
            public PARAMDESC paramdesc;

            public _ELEMDESC() {
            }

            public _ELEMDESC(Pointer pointer) {
                super(pointer);
                setType("paramdesc");
                this.read();
            }

            /**
             * @param paramdesc
             *            info about the parameter<br>
             *            C type : PARAMDESC
             */
            public _ELEMDESC(PARAMDESC paramdesc) {
                this.paramdesc = paramdesc;
                setType("paramdesc");
            }

            /**
             * @param idldesc
             *            info for remoting the element<br>
             *            C type : IDLDESC
             */
            public _ELEMDESC(IDLDESC idldesc) {
                this.idldesc = idldesc;
                setType("idldesc");
            }
        };

        public ELEMDESC() {
            super();
        }

        public ELEMDESC(Pointer pointer) {
            super(pointer);
            this.read();
        }

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    }

    public static class FUNCKIND extends Structure {
        public static class ByReference extends FUNCKIND implements
                Structure.ByReference {
        };

        // / <i>native declaration : line 20</i>
        public static final int FUNC_VIRTUAL = 0;
        // / <i>native declaration : line 21</i>
        public static final int FUNC_PUREVIRTUAL = FUNC_VIRTUAL + 1;
        // / <i>native declaration : line 22</i>
        public static final int FUNC_NONVIRTUAL = FUNC_PUREVIRTUAL + 1;
        // / <i>native declaration : line 23</i>
        public static final int FUNC_STATIC = FUNC_NONVIRTUAL + 1;
        // / <i>native declaration : line 24</i>
        public static final int FUNC_DISPATCH = FUNC_STATIC + 1;

        public static final List<String> FIELDS = createFieldsOrder("value");

        public int value;

        public FUNCKIND() {
            super();
        }

        public FUNCKIND(int value) {
            this.value = value;

        }

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    };

    public static class INVOKEKIND extends Structure {
        public static class ByReference extends INVOKEKIND implements
                Structure.ByReference {
        };

        // / <i>native declaration : line 30</i>
        public static final INVOKEKIND INVOKE_FUNC = new INVOKEKIND(1);
        // / <i>native declaration : line 31</i>
        public static final INVOKEKIND INVOKE_PROPERTYGET = new INVOKEKIND(2);
        // / <i>native declaration : line 32</i>
        public static final INVOKEKIND INVOKE_PROPERTYPUT = new INVOKEKIND(4);
        // / <i>native declaration : line 33</i>
        public static final INVOKEKIND INVOKE_PROPERTYPUTREF = new INVOKEKIND(8);

        public static final List<String> FIELDS = createFieldsOrder("value");
        public int value;

        public INVOKEKIND() {
            super();
        }

        public INVOKEKIND(int value) {
            this.value = value;

        }

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    };

    public static class CALLCONV extends Structure {
        public static class ByReference extends CALLCONV implements
                Structure.ByReference {
        };

        public static final List<String> FIELDS = createFieldsOrder("value");

        // / <i>native declaration : line 4</i>
        public static final int CC_FASTCALL = 0;
        // / <i>native declaration : line 5</i>
        public static final int CC_CDECL = 1;
        // / <i>native declaration : line 6</i>
        public static final int CC_MSCPASCAL = CALLCONV.CC_CDECL + 1;
        // / <i>native declaration : line 7</i>
        public static final int CC_PASCAL = CALLCONV.CC_MSCPASCAL;
        // / <i>native declaration : line 8</i>
        public static final int CC_MACPASCAL = CALLCONV.CC_PASCAL + 1;
        // / <i>native declaration : line 9</i>
        public static final int CC_STDCALL = CALLCONV.CC_MACPASCAL + 1;
        // / <i>native declaration : line 10</i>
        public static final int CC_FPFASTCALL = CALLCONV.CC_STDCALL + 1;
        // / <i>native declaration : line 11</i>
        public static final int CC_SYSCALL = CALLCONV.CC_FPFASTCALL + 1;
        // / <i>native declaration : line 12</i>
        public static final int CC_MPWCDECL = CALLCONV.CC_SYSCALL + 1;
        // / <i>native declaration : line 13</i>
        public static final int CC_MPWPASCAL = CALLCONV.CC_MPWCDECL + 1;
        // / <i>native declaration : line 14</i>
        public static final int CC_MAX = CALLCONV.CC_MPWPASCAL + 1;

        public int value;

        public CALLCONV() {
        }

        public CALLCONV(int value) {
            this.value = value;
        }

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    };

    public static class VARKIND extends Structure {
        public static class ByReference extends VARKIND implements
                Structure.ByReference {
        };

        // / <i>native declaration : line 4</i>
        public static final int VAR_PERINSTANCE = 0;
        // / <i>native declaration : line 5</i>
        public static final int VAR_STATIC = VAR_PERINSTANCE + 1;
        // / <i>native declaration : line 6</i>
        public static final int VAR_CONST = VAR_STATIC + 1;
        // / <i>native declaration : line 7</i>
        public static final int VAR_DISPATCH = VAR_CONST + 1;

        public static final List<String> FIELDS = createFieldsOrder("value");

        public int value;

        public VARKIND() {
            super();
        }

        public VARKIND(int value) {
            this.value = value;
        }

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    };

    public static class TYPEDESC extends Structure {
        public static class ByReference extends TYPEDESC implements
                Structure.ByReference {
        };


        public static class _TYPEDESC extends Union {
            /**
             * [case()]<br>
             * C type : tagTYPEDESC*
             */
            public TYPEDESC.ByReference lptdesc;
            /**
             * [case()]<br>
             * C type : tagARRAYDESC*
             */
            public ARRAYDESC.ByReference lpadesc;
            /**
             * [case()]<br>
             * C type : HREFTYPE
             */
            public HREFTYPE hreftype;

            public _TYPEDESC() {
                this.setType("hreftype");
                this.read();
            }

            public _TYPEDESC(Pointer pointer) {
                super(pointer);
                this.setType("hreftype");
                this.read();
            }

            public TYPEDESC.ByReference getLptdesc() {
                this.setType("lptdesc");
                this.read();
                return this.lptdesc;
            }

            public ARRAYDESC.ByReference getLpadesc() {
                this.setType("lpadesc");
                this.read();
                return this.lpadesc;
            }

            public HREFTYPE getHreftype() {
                this.setType("hreftype");
                this.read();
                return this.hreftype;
            }
        };

        public static final List<String> FIELDS = createFieldsOrder("_typedesc", "vt");
        public _TYPEDESC _typedesc;
        public VARTYPE vt;

        public TYPEDESC() {
            this.read();
        }

        public TYPEDESC(Pointer pointer) {
            super(pointer);
            this.read();
        }

        public TYPEDESC(_TYPEDESC _typedesc, VARTYPE vt) {
            this._typedesc = _typedesc;
            this.vt = vt;
        }

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    }

    public static class IDLDESC extends Structure {
        public static class ByReference extends IDLDESC implements
                Structure.ByReference {

            public ByReference() {
                super();
            }

            public ByReference(IDLDESC idldesc) {
                super(idldesc.dwReserved, idldesc.wIDLFlags);
            }
        };

        public static final List<String> FIELDS = createFieldsOrder("dwReserved", "wIDLFlags");

        // / C type : ULONG_PTR
        public ULONG_PTR dwReserved;
        public USHORT wIDLFlags;

        public IDLDESC() {
            super();
        }

        public IDLDESC(Pointer pointer) {
            super(pointer);
            this.read();
        }

        // / @param dwReserved C type : ULONG_PTR
        public IDLDESC(ULONG_PTR dwReserved, USHORT wIDLFlags) {
            this.dwReserved = dwReserved;
            this.wIDLFlags = wIDLFlags;
        }

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    }

    public class ARRAYDESC extends Structure {
        public static final List<String> FIELDS = createFieldsOrder("tdescElem", "cDims", "rgbounds");
        // / C type : TYPEDESC
        public TYPEDESC tdescElem;
        public short cDims;
        /**
         * [size_is]<br>
         * C type : SAFEARRAYBOUND[1]
         */
        public SAFEARRAYBOUND[] rgbounds = { new SAFEARRAYBOUND() };

        public ARRAYDESC() {
            super();
        }

        public ARRAYDESC(Pointer pointer) {
            super(pointer);
            this.read();
        }

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }

        /**
         * @param tdescElem
         *            C type : TYPEDESC<br>
         * @param cDims dimensions
         * @param rgbounds
         *            [size_is]<br>
         *            C type : SAFEARRAYBOUND[1]
         */
        public ARRAYDESC(TYPEDESC tdescElem, short cDims, SAFEARRAYBOUND rgbounds[]) {
            this.tdescElem = tdescElem;
            this.cDims = cDims;
            if (rgbounds.length != this.rgbounds.length)
                throw new IllegalArgumentException("Wrong array size !");
            this.rgbounds = rgbounds;
        }

        public static class ByReference extends ARRAYDESC implements
                Structure.ByReference {

        };
    }

    public static class PARAMDESC extends Structure {
        public static class ByReference extends PARAMDESC implements
                Structure.ByReference {
        };

        public static final List<String> FIELDS = createFieldsOrder("pparamdescex", "wParamFlags");

        // replaced PARAMDESCEX.ByReference with Pointer
        // because of JNA 4 has a problem with ByReference
        public Pointer pparamdescex;
        public USHORT wParamFlags;

        public PARAMDESC() {
            super();
        }

        public PARAMDESC(Pointer pointer) {
            super(pointer);
            this.read();
        }

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    }

    public static class PARAMDESCEX extends Structure {
        public static class ByReference extends PARAMDESCEX implements
                Structure.ByReference {
        };

        public static final List<String> FIELDS = createFieldsOrder("cBytes", "varDefaultValue");

        public ULONG cBytes;
        public VariantArg varDefaultValue;

        public PARAMDESCEX() {
            super();
        }

        public PARAMDESCEX(Pointer pointer) {
            super(pointer);
            this.read();
        }

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    }

    public static class HREFTYPE extends DWORD {
        private static final long serialVersionUID = 1L;

        public HREFTYPE() {
            super();
        }

        public HREFTYPE(long value) {
            super(value);
        }
    }

    public static class HREFTYPEByReference extends DWORDByReference {
        public HREFTYPEByReference() {
            this(new HREFTYPE(0));
        }

        public HREFTYPEByReference(DWORD value) {
            super(value);
        }

        public void setValue(HREFTYPE value) {
            getPointer().setInt(0, value.intValue());
        }

        @Override
        public HREFTYPE getValue() {
            return new HREFTYPE(getPointer().getInt(0));
        }
    }

    public class TYPEATTR extends Structure {
        public static class ByReference extends TYPEATTR implements
                Structure.ByReference {
        };

        public static final List<String> FIELDS = createFieldsOrder("guid", "lcid", "dwReserved", "memidConstructor",
                "memidDestructor", "lpstrSchema", "cbSizeInstance",
                "typekind", "cFuncs", "cVars", "cImplTypes",
                "cbSizeVft", "cbAlignment", "wTypeFlags",
                "wMajorVerNum", "wMinorVerNum", "tdescAlias",
                "idldescType");

        // / C type : GUID
        public GUID guid;
        // / C type : LCID
        public LCID lcid;
        public DWORD dwReserved;
        // / C type : MEMBERID
        public MEMBERID memidConstructor;
        // / C type : MEMBERID
        public MEMBERID memidDestructor;
        // / C type : LPOLESTR
        public LPOLESTR lpstrSchema;
        public ULONG cbSizeInstance;
        // / C type : TYPEKIND
        public TYPEKIND typekind;
        public WORD cFuncs;
        public WORD cVars;
        public WORD cImplTypes;
        public WORD cbSizeVft;
        public WORD cbAlignment;
        public WORD wTypeFlags;
        public WORD wMajorVerNum;
        public WORD wMinorVerNum;
        // / C type : TYPEDESC
        public TYPEDESC tdescAlias;
        // / C type : IDLDESC
        public IDLDESC idldescType;

        public TYPEATTR() {
            super();
        }

        public TYPEATTR(Pointer pointer) {
            super(pointer);
            this.read();
        }

        @Override
        protected List<String> getFieldOrder() {
            return FIELDS;
        }
    }
}

```

## Error
OaIdl.INVOKEKIND can't be instantiated (fixes failing TypeLibUtilTest)

## Error Description
The initialization order of the static fields in OaIdl.INVOKEKIND is broken. When INVOKEKIND is initialized the static fields also hold instances of INVOKEKIND. The constructors are called before the necessary definition of FIELDS is available. This results in the stacktrace:

**java.lang.ExceptionInInitializerError
    at java.lang.reflect.Constructor.newInstance(Constructor.java:422)
    at java.lang.Class.newInstance(Class.java:442)
    at com.sun.jna.Structure.newInstance(Structure.java:1807)**
    at com.sun.jna.Structure.newInstance(Structure.java:1793)
    at com.sun.jna.Structure.size(Structure.java:1062)
    at com.sun.jna.Native.getNativeSize(Native.java:1208)
    at com.sun.jna.Structure.getNativeSize(Structure.java:2114)
    at com.sun.jna.Structure.getNativeSize(Structure.java:2104)
    at com.sun.jna.Structure.validateField(Structure.java:1138)
    at com.sun.jna.Structure.validateFields(Structure.java:1151)
    at com.sun.jna.Structure.<init>(Structure.java:178)
    at com.sun.jna.Structure.<init>(Structure.java:171)
    at com.sun.jna.Structure.<init>(Structure.java:167)
    at com.sun.jna.platform.win32.OaIdl$FUNCDESC.<init>(OaIdl.java:815)
    at com.sun.jna.platform.win32.COM.TypeInfoUtil.getFuncDesc(TypeInfoUtil.java:102)
    at com.sun.jna.platform.win32.COM.TypeLibUtilTest.testBug(TypeLibUtilTest.java:86)
**Caused by: java.lang.NullPointerException
    at com.sun.jna.Structure.getFields(Structure.java:996)**
    at com.sun.jna.Structure.deriveLayout(Structure.java:116

