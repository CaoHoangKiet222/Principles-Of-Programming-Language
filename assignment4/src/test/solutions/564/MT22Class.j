.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is f [Ljava/lang/String; from Label0 to Label1
	iconst_5
	anewarray java/lang/String
	dup
	iconst_0
	ldc "kiet"
	aastore
	dup
	iconst_1
	ldc ""
	aastore
	dup
	iconst_2
	ldc ""
	aastore
	astore_1
	aload_1
	iconst_0
	aaload
	invokestatic io/printString(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
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
