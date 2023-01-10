import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    # # # Test Comment # # #
    def test_1(self):
        input = "/* hello world \t\b\n Hello World*/"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 101))

    def test_2(self):
        input = """// hello world"""
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 102))

    def test_3(self):
        input = "// hello world\n\t/*Hello world*/"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 103))

    def test_4(self):
        input = "// x/*x*/"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 104))

    def test_5(self):
        input = "/* \n\t//x */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 105))

    def test_6(self):
        input = "/* \n\t/*x*/ */"
        expect = "*,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 106))

    # Test Identifiers
    def test_7(self):
        input = "abc"
        expect = "abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 107))

    def test_8(self):
        input = "abc a12"
        expect = "abc,a12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 108))

    def test_9(self):
        input = "xyz A12"
        expect = "xyz,A12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 109))

    def test_10(self):
        input = "abc?svn"
        expect = "abc,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 110))

    def test_11(self):
        input = "0a12"
        expect = "0,a12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 111))

    def test_12(self):
        input = "_0a12"
        expect = "_0a12,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 112))

    # # # Test Int Literals # # #
    def test_13(self):
        input = "0 12 321 20342324"
        expect = "0,12,321,20342324,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 113))

    def test_14(self):
        input = "0 12_321 20_342_324"
        expect = "0,12321,20342324,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 114))

    def test_15(self):
        input = "1_234_567_"
        expect = "1234567,_,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 115))

    def test_16(self):
        input = "-323"
        expect = "-,323,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 116))

    # # # Test Float Literals # # #
    def test_17(self):
        input = "0.0"
        expect = "0.0,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 117))

    def test_18(self):
        input = "1.001"
        expect = "1.001,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 118))

    def test_19(self):
        input = "0.200000"
        expect = "0.200000,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 119))

    def test_20(self):
        input = "1_234.567"
        expect = "1234.567,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 120))

    def test_21(self):
        input = "1_234."
        expect = "1234.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 121))

    def test_22(self):
        input = "11e8 0.37E-3 123e+41 1_2_8e-42"
        expect = "11e8,0.37E-3,123e+41,128e-42,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 122))

    # # # Test String Literals # # #
    def test_23(self):
        input = "\"This is a string containing tab \t\""
        expect = "This is a string containing tab \t,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 123))

    def test_24(self):
        input = "\"He asked me: \\\"Where is John?\\\"\""
        expect = "He asked me: \\\"Where is John?\\\",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 124))

    def test_25(self):
        input = "\"He asked me: \'\"Where is John?\'\"\""
        expect = "He asked me: \'\"Where is John?\'\",<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 125))

    # # # Test Unclosed String Literals # # #
    def test_26(self):
        input = "\"a"
        expect = "Unclosed String: a"
        self.assertTrue(TestLexer.test(input, expect, 126))

    def test_27(self):
        input = "\"abc \\n \\f 's def"
        expect = "Unclosed String: abc \\n \\f 's def"
        self.assertTrue(TestLexer.test(input, expect, 127))

    def test_28(self):
        input = "\"x \\b y"
        expect = "Unclosed String: x \\b y"
        self.assertTrue(TestLexer.test(input, expect, 128))

    def test_29(self):
        input = "\"It is an unclosed \\n string"
        expect = "Unclosed String: It is an unclosed \\n string"
        self.assertTrue(TestLexer.test(input, expect, 129))

    def test_30(self):
        input = "\"This is a \\t string \\n containing tab \" \"He asked \\n me: '\"Where '\"is'\" John?'\"\" \"I am not closed"
        expect = "This is a \\t string \\n containing tab ,He asked \\n me: '\"Where '\"is'\" John?'\",Unclosed String: I am not closed"
        self.assertTrue(TestLexer.test(input, expect, 130))

    # # # Test Illegal ESC # # #
    def test_31(self):
        input = "\"Escape sequence \'\"Here it is \\k\'\"\""
        expect = "Illegal Escape In String: Escape sequence \'\"Here it is \k"
        self.assertTrue(TestLexer.test(input, expect, 131))

    def test_32(self):
        input = "\"\\x\""
        expect = "Illegal Escape In String: \\x"
        self.assertTrue(TestLexer.test(input, expect, 132))

    def test_33(self):
        input = "\"\\\\ I am a \\\\ \\\' 21-year-old man \\a\""
        expect = "Illegal Escape In String: \\\\ I am a \\\\ \\\' 21-year-old man \\a"
        self.assertTrue(TestLexer.test(input, expect, 133))

    def test_34(self):
        input = "\" \b \\a \t \f \r\""
        expect = "Illegal Escape In String:  \b \\a"
        self.assertTrue(TestLexer.test(input, expect, 134))

    # # # Test Boolean Literals # # #
    def test_35(self):
        input = "true"
        expect = "true,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 135))

    def test_36(self):
        input = "false"
        expect = "false,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 136))

    def test_37(self):
        input = "truefalse"
        expect = "truefalse,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 137))

    # # # Test Operators # # #
    def test_38(self):
        input = "==="
        expect = "==,=,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 138))

    def test_39(self):
        input = "===="
        expect = "==,==,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 139))

    def test_40(self):
        input = "||||"
        expect = "||,||,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 140))

    def test_41(self):
        input = "&&&"
        expect = "&&,Error Token &"
        self.assertTrue(TestLexer.test(input, expect, 141))

    def test_42(self):
        input = "|||"
        expect = "||,Error Token |"
        self.assertTrue(TestLexer.test(input, expect, 142))

    def test_43(self):
        input = "*/%::!=!<===+-"
        expect = "*,/,%,::,!=,!,<=,==,+,-,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 143))

    def test_44(self):
        input = "*/%::!=!<===+-"
        expect = "*,/,%,::,!=,!,<=,==,+,-,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 144))

    def test_45(self):
        input = "-5_7"
        expect = "-,57,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 145))

    def test_46(self):
        input = "-5_7+785"
        expect = "-,57,+,785,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 146))

    def test_47(self):
        input = "a <= b && a > c + d"
        expect = "a,<=,b,&&,a,>,c,+,d,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 147))

    def test_48(self):
        input = "@ >= 2"
        expect = "Error Token @"
        self.assertTrue(TestLexer.test(input, expect, 148))

    def test_49(self):
        input = "a[2]::b"
        expect = "a,[,2,],::,b,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 149))

    # # # Test Seperators # # #
    def test_50(self):
        input = "(){}[].,;:="
        expect = "(,),{,},[,],.,,,;,:,=,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 150))

    def test_51(self):
        input = "x[(a + b)]"
        expect = "x,[,(,a,+,b,),],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 151))

    def test_52(self):
        input = "x[(1_234e+34 - y)]"
        expect = "x,[,(,1234e+34,-,y,),],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 152))

    # # # Test Keywords # # #
    def test_53(self):
        input = "auto boolean integer float string array break do else if function for return void out continue while of inherit"
        expect = "auto,boolean,integer,float,string,array,break,do,else,if,function,for,return,void,out,continue,while,of,inherit,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 153))

    def test_54(self):
        input = "auto x = 2;"
        expect = "auto,x,=,2,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 154))

    def test_55(self):
        input = "boolean x = true;"
        expect = "boolean,x,=,true,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 155))

    def test_56(self):
        input = "integer a = 1;float b = 1.0;"
        expect = "integer,a,=,1,;,float,b,=,1.0,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 156))

    def test_57(self):
        input = """
        fact : function int (n : int) {
            if (n == 0) return 1;
            else return n*fact(n-1);
        }
        """
        expect = "fact,:,function,int,(,n,:,int,),{,if,(,n,==,0,),return,1,;,else,return,n,*,fact,(,n,-,1,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 157))

    def test_58(self):
        input = """
        main : function void () {
            delta : int = fact(3);
            inc (x, delta);
            printint(x);
        }
        """
        expect = "main,:,function,void,(,),{,delta,:,int,=,fact,(,3,),;,inc,(,x,,,delta,),;,printint,(,x,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 158))

    def test_59(self):
        input = """
        inc : function void (out n: int, delta : int) {
            n = n + delta;
        }
        """
        expect = "inc,:,function,void,(,out,n,:,int,,,delta,:,int,),{,n,=,n,+,delta,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 159))

    # # # Test variable declaration # # #
    def test_60(self):
        input = """
        a, b, c : array [2, 3] of int;
        """
        expect = "a,,,b,,,c,:,array,[,2,,,3,],of,int,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 160))

    def test_61(self):
        input = """
        a, b, c : auto = 1, 1.0, 1.1;
        """
        expect = "a,,,b,,,c,:,auto,=,1,,,1.0,,,1.1,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 161))

    def test_62(self):
        input = """
        a, b, c : string = \"abc\", \"xyz\", \"ooo\";
        """
        expect = "a,,,b,,,c,:,string,=,abc,,,xyz,,,ooo,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 162))

    # # # Test Parameters # # #
    def test_63(self):
        input = """
        out x : int
        """
        expect = "out,x,:,int,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 163))

    def test_64(self):
        input = """
        x : int, y : string, z : array [2, 3] of integer
        """
        expect = "x,:,int,,,y,:,string,,,z,:,array,[,2,,,3,],of,integer,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 164))

    # # # Test Function declarations # # #
    def test_65(self):
        input = """
        hello : function void () {
            print();
        }
        """
        expect = "hello,:,function,void,(,),{,print,(,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 165))

    # # # Test Function Call # # #
    def test_66(self):
        input = """
            print(a, b, c);
        """
        expect = "print,(,a,,,b,,,c,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 166))

    def test_67(self):
        input = """
            print(a, b[2] + c[3], d);
        """
        expect = "print,(,a,,,b,[,2,],+,c,[,3,],,,d,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 167))

    # # # Test statements # # #
    def test_68(self):
        input = """
        a = 2; b = 3.e2; c = false;
        """
        expect = "a,=,2,;,b,=,3.e2,;,c,=,false,;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 168))

    def test_69(self):
        input = """
        if (2 == 3) {
            print("hello");
        }
        """
        expect = "if,(,2,==,3,),{,print,(,hello,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 169))

    def test_70(self):
        input = """
        if (a == 3) {
            print("hello");
        } else {
            foo(a);
        }
        """
        expect = "if,(,a,==,3,),{,print,(,hello,),;,},else,{,foo,(,a,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 170))

    def test_71(self):
        input = """
        for (i = 1, i < 10, i + 1) {
            writeInt(i);
        }
"""
        expect = "for,(,i,=,1,,,i,<,10,,,i,+,1,),{,writeInt,(,i,),;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 171))

    def test_72(self):
        input = """
        int a = 0;
        do {
            writeInt(a);
            a++;
        }
        while (a != 3);
"""
        expect = "int,a,=,0,;,do,{,writeInt,(,a,),;,a,+,+,;,},while,(,a,!=,3,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 172))

    def test_73(self):
        input = """
        int a = 0;
        while (a != 3) {
            process(a, "Ok");
            a++;
        }
"""
        expect = "int,a,=,0,;,while,(,a,!=,3,),{,process,(,a,,,Ok,),;,a,+,+,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 173))

    def test_74(self):
        input = """
        for (i = 1, i < 10, i + 1) {
            if (i == 8) {
                break;
            }
        }
"""
        expect = "for,(,i,=,1,,,i,<,10,,,i,+,1,),{,if,(,i,==,8,),{,break,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 174))

    def test_75(self):
        input = """
        for (i = 1, i < 10, i + 1) {
            if (i == 8) {
                break;
            }
            if (i == 6) {
                continue;
            }
        }
"""
        expect = "for,(,i,=,1,,,i,<,10,,,i,+,1,),{,if,(,i,==,8,),{,break,;,},if,(,i,==,6,),{,continue,;,},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 175))

    def test_76(self):
        input = """
        return foo(x+1, y+2);
"""
        expect = "return,foo,(,x,+,1,,,y,+,2,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 176))

    def test_77(self):
        input = """
        return a + b;
        return c[1, 2] + d[1, 3];
"""
        expect = "return,a,+,b,;,return,c,[,1,,,2,],+,d,[,1,,,3,],;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 177))

    def test_78(self):
        input = """
        foo(a + b);
        foo(2 + x, 4.0 / y);
        goo();
"""
        expect = "foo,(,a,+,b,),;,foo,(,2,+,x,,,4.0,/,y,),;,goo,(,),;,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 178))

    def test_79(self):
        input = """
        {
            r, s: int;
            r = 2.0;
            a, b: array [5] of int;
            s = r * r * myPI;
            a[0] = s;
        }
"""
        expect = "{,r,,,s,:,int,;,r,=,2.0,;,a,,,b,:,array,[,5,],of,int,;,s,=,r,*,r,*,myPI,;,a,[,0,],=,s,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 179))

    def test_80(self):
        input = """
        {
            r, s: int;
            r = 2.0;
            a, b: array [5] of int;
            s = r * r * myPI;
            a[0] = s;
        }
"""
        expect = "{,r,,,s,:,int,;,r,=,2.0,;,a,,,b,:,array,[,5,],of,int,;,s,=,r,*,r,*,myPI,;,a,[,0,],=,s,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 180))

    # # # Test mix # # #
    def test_81(self):
        input = """
        hello : function void () {
            // " abc \f  xyz "
            // print();
        }
"""
        expect = "hello,:,function,void,(,),{,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 181))

    def test_82(self):
        input = """
        s : string;
        hello : function void () {
            s = "hello"
        }
"""
        expect = "s,:,string,;,hello,:,function,void,(,),{,s,=,hello,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 182))

    def test_83(self):
        input = """
         powerFunc : function int (base : int, power : int) {
          if (power == 0)
            return 1;
          else
            return (base * powerFunc(base, power - 1));
        }

        mod: function int (num: array [5] of int , a: int) {
          res, i : int  = 0, -1;

          for (i = 0; i < 5; i+1)
            res = (res * 10 + num[i] - "0") % a;

          return res;
        }
"""
        expect = "powerFunc,:,function,int,(,base,:,int,,,power,:,int,),{,if,(,power,==,0,),return,1,;,else,return,(,base,*,powerFunc,(,base,,,power,-,1,),),;,},mod,:,function,int,(,num,:,array,[,5,],of,int,,,a,:,int,),{,res,,,i,:,int,=,0,,,-,1,;,for,(,i,=,0,;,i,<,5,;,i,+,1,),res,=,(,res,*,10,+,num,[,i,],-,0,),%,a,;,return,res,;,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 183))

    def test_84(self):
        input = r"""
    int foo();
        while false{
            hard_work();
                if true then break;
            }
"""
        expect = r"""int,foo,(,),;,while,false,{,hard_work,(,),;,if,true,then,break,;,},<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 184))

    def test_85(self):
        input = """
        /*=====================
        Comment here
        ====================={{{{{{}}}}}}}}}}}
"""
        expect = "/,*,==,==,==,==,==,==,==,==,==,==,=,Comment,here,==,==,==,==,==,==,==,==,==,==,=,{,{,{,{,{,{,},},},},},},},},},},},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 185))

    def test_86(self):
        input = """
        int y = a|b;
"""
        expect = "int,y,=,a,Error Token |"
        self.assertTrue(TestLexer.test(input, expect, 186))

    def test_87(self):
        input = """
        abc ABC aBC Abc _ABC __ABc __123ABc
        h98f394__VWT_b5_VT_YGU87udhf__T_
"""
        expect = "abc,ABC,aBC,Abc,_ABC,__ABc,__123ABc,h98f394__VWT_b5_VT_YGU87udhf__T_,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 187))

    def test_88(self):
        input = """
    123abc 123_abc 00000123_123abc
"""
        expect = "123,abc,123,_abc,0,0,0,0,0,123123,abc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 188))

    def test_89(self):
        input = """
    {xsaklf_seoirw + kljwer + 2324}
    {1, 2, 3_lskdjflskd}
    {2.3 + 3.2, 4.2, 102e3}
"""
        expect = "{,xsaklf_seoirw,+,kljwer,+,2324,},{,1,,,2,,,3,_lskdjflskd,},{,2.3,+,3.2,,,4.2,,,102e3,},<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 189))

    def test_90(self):
        input = """
    "Formfeed   \f"
"""
        expect = "Formfeed   \f,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 190))

    def test_91(self):
        input = """
"Newline sadfasdkfjl askdjflkasdf s dlfsldfjas dlfsldkf klj eiwoei
	multiple lines skdjfw ioueow
    lksjdlf
    klsldfjlasdjflasdf 
" 
"""
        expect = "Unclosed String: Newline sadfasdkfjl askdjflkasdf s dlfsldfjas dlfsldkf klj eiwoei"
        self.assertTrue(TestLexer.test(input, expect, 191))

    def test_92(self):
        input = """
        00001.1111000000
        0e-432309123
        000000001e-40000
"""
        expect = "0,0,0,0,1.1111000000,0e-432309123,0,0,0,0,0,0,0,0,1e-40000,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 192))

    def test_93(self):
        input = """
        "abc - xyz"
        "abc \ xyz"
"""
        expect = "abc - xyz,Illegal Escape In String: abc \ "
        self.assertTrue(TestLexer.test(input, expect, 193))

    def test_94(self):
        input = """
    s = "string 
    "
    a = 4
    g = 9
"""
        expect = "s,=,Unclosed String: string "
        self.assertTrue(TestLexer.test(input, expect, 194))

    def test_95(self):
        input = """
Break, Continue, If, Elseif
"""
        expect = "Break,,,Continue,,,If,,,Elseif,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 195))

    def test_96(self):
        input = """
    \"This is a \\t string \\n containing tab \" \"He asked \\n me: '\"Where '\"is'\" John?'\"\" \"I am not closed"
"""
        expect = """This is a \\t string \\n containing tab ,He asked \\n me: '"Where '"is'" John?'",I am not closed,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 196))

    def test_97(self):
        input = """
    /* This is a block comment */
// This is a line comment
    /* Comment with multiple lines
        Hello comments
    */
    /*
        Comment multiple lines
    */
    /* nest comments /*
    block 
    comment
        // inline comment
    */
// inline comment /* block 
    comment */
    */
"""
        expect = "comment,*,/,*,/,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 197))

    def test_98(self):
        input = """
	/* This is a block comment */
    /*
        Comment multiple lines
        Line 1
        Line 2
        Line 3
    */
"""
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 198))

    def test_99(self):
        input = """
        12.
        12.e05
        12.e-05
        12.05e05
        12.05e-05
        12.05
        .05
        .05e05
        .05e-05
"""
        expect = "12.,12.e05,12.e-05,12.05e05,12.05e-05,12.05,.05,.05e05,.05e-05,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 199))

    def test_100(self):
        input = """
    \\ // / \
"""
        expect = "Error Token \\"
        self.assertTrue(TestLexer.test(input, expect, 200))
