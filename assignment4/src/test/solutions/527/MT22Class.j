.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static arr1 [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MT22Class.arr1 [I
	iconst_1
	iconst_2
	iadd
	iconst_1
	iaload
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 3
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
	iconst_2
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_3
	iastore
	dup
	iconst_2
	bipush 123
	iastore
	dup
	iconst_3
	sipush 1238
	iastore
	putstatic MT22Class.arr1 [I
Label1:
	return
.limit stack 4
.limit locals 0
.end method
