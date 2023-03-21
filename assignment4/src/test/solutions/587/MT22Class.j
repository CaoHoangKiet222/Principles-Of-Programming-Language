.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static gcdIteration(II)I
.var 0 is p I from Label0 to Label1
.var 1 is q I from Label0 to Label1
Label0:
Label2:
	iload_0
	iload_1
	imul
	iconst_0
	if_icmpeq Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	iload_0
	iload_1
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	iload_1
	iload_0
	irem
	istore_1
	goto Label11
Label10:
	iload_0
	iload_1
	irem
	istore_0
Label11:
Label4:
	goto Label2
Label3:
Label5:
	iload_0
	iload_1
	iadd
	ireturn
Label1:
.limit stack 6
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 12
	bipush 6
	invokestatic MT22Class/gcdIteration(II)I
	invokestatic io/printInteger(I)V
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
