.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_1
	istore_1
.var 2 is x [I from Label0 to Label1
	bipush 100
	newarray int
	astore_2
	iload_1
	iconst_2
	irem
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	aload_2
	iload_1
	bipush 10
	imul
	iconst_0
	iadd
	iload_1
	iastore
	goto Label5
Label4:
	aload_2
	iconst_0
	bipush 10
	imul
	iload_1
	iadd
	iload_1
	iconst_1
	iadd
	iastore
Label5:
	aload_2
	iconst_0
	bipush 10
	imul
	iload_1
	iadd
	iaload
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 9
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
