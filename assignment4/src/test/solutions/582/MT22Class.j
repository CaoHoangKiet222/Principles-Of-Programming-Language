.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static max_two_nums(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iload_0
	iload_1
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	goto Label5
Label4:
	iload_0
	ireturn
Label5:
	iload_1
	ireturn
Label1:
.limit stack 3
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n I from Label0 to Label1
	bipush 10
	istore_1
.var 2 is m I from Label0 to Label1
	bipush 11
	istore_2
	iload_1
	iload_2
	invokestatic MT22Class/max_two_nums(II)I
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 2
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
