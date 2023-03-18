.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_5
	istore_1
.var 2 is x [I from Label0 to Label1
	bipush 100
	newarray int
	dup
	iconst_0
	bipush 101
	iastore
	dup
	iconst_1
	sipush 202
	iastore
	dup
	bipush 10
	iload_1
	iastore
	astore_2
	aload_2
	bipush 10
	iaload
	invokestatic io/printInteger(I)V
	iload_1
	iconst_2
	irem
	iconst_0
	if_icmpeq Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	aload_2
	bipush 50
	iload_1
	iastore
	goto Label5
Label4:
	aload_2
	iconst_5
	iload_1
	iconst_1
	iadd
	iastore
Label5:
	aload_2
	bipush 50
	iaload
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 12
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
