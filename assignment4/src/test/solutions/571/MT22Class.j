.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static inc(II)I
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
Label2:
	iload_0
	iconst_0
	if_icmpeq Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	iload_0
	iconst_1
	isub
	istore_0
Label4:
	goto Label2
Label3:
Label5:
Label8:
	iload_1
	iconst_1
	iadd
	istore_0
Label10:
	iload_0
	iload_1
	if_icmpgt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label9
	goto Label8
Label9:
Label11:
	iload_0
	ireturn
Label1:
.limit stack 5
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is b I from Label0 to Label1
	bipush 10
	istore_1
.var 2 is a I from Label0 to Label1
	iconst_3
	istore_2
	iload_2
	iconst_5
	bipush 10
	invokestatic MT22Class/inc(II)I
	iadd
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 5
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
