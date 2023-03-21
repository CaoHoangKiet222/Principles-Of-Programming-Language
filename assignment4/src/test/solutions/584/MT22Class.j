.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static factorial(I)I
.var 0 is N I from Label0 to Label1
Label0:
.var 1 is result I from Label0 to Label1
	iconst_1
	istore_1
.var 2 is i I from Label0 to Label1
	iconst_1
	istore_2
Label2:
	iload_2
	iload_0
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
Label8:
	iload_1
	iload_2
	imul
	istore_1
Label9:
Label4:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label2
Label3:
Label5:
	iload_1
	ireturn
Label1:
.limit stack 4
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n I from Label0 to Label1
	bipush 10
	istore_1
	iload_1
	invokestatic MT22Class/factorial(I)I
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 1
.limit locals 2
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
