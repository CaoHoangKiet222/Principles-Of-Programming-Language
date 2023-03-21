.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static fibonacci(I)I
.var 0 is n I from Label0 to Label1
Label0:
.var 1 is f0 I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is f1 I from Label0 to Label1
	iconst_1
	istore_2
.var 3 is fn I from Label0 to Label1
	iconst_1
	istore_3
	iload_0
	iconst_0
	if_icmpge Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	goto Label5
Label4:
	iconst_1
	ineg
	ireturn
Label5:
	iload_0
	iconst_0
	iload_0
	iconst_1
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ior
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
.var 4 is i I from Label0 to Label1
	iconst_2
	istore 4
Label12:
	iload 4
	iload_0
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label13
Label18:
	iload_2
	istore_1
	iload_3
	istore_2
	iload_1
	iload_2
	iadd
	istore_3
Label19:
Label14:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label12
Label13:
Label15:
	goto Label11
Label10:
	iload_0
	ireturn
Label11:
	iload_3
	ireturn
Label1:
.limit stack 10
.limit locals 5
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	invokestatic MT22Class/fibonacci(I)I
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 1
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
