.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label2:
.var 2 is j I from Label0 to Label1
	iconst_0
	istore_2
Label6:
	iload_2
	bipush 20
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifle Label7
	iload_1
	iload_2
	iadd
	bipush 20
	if_icmplt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label15
Label14:
	goto Label9
Label15:
Label8:
	goto Label6
Label7:
Label9:
	iload_2
	invokestatic io/printInteger(I)V
	iload_1
	iconst_1
	iadd
	istore_1
Label4:
	iload_1
	bipush 10
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label3
	goto Label2
Label3:
Label5:
Label1:
	return
.limit stack 7
.limit locals 3
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
