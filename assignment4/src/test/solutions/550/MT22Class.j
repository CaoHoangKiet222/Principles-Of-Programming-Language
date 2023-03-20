.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static inc(II)F
.var 0 is n I from Label0 to Label1
.var 1 is delta I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	istore_0
.var 2 is i I from Label0 to Label1
	iconst_1
	istore_2
Label2:
	iload_2
	iload_0
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
Label8:
.var 3 is j I from Label8 to Label9
	iconst_1
	istore_3
Label10:
	iload_3
	iload_0
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label11
Label16:
	iload_2
	iload_3
	iadd
	iconst_5
	if_icmplt Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifgt Label20
	iload_2
	iload_3
	isub
	invokestatic io/printInteger(I)V
	goto Label21
Label20:
	iload_2
	iload_3
	iadd
	i2f
	freturn
Label21:
Label17:
Label12:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label10
Label11:
Label13:
Label9:
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label5:
	bipush 10
	i2f
	freturn
Label1:
.limit stack 8
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	iconst_2
	invokestatic MT22Class/inc(II)F
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LMT22Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
