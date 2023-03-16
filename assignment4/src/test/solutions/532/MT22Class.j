.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static x [F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MT22Class.x [F
	iconst_2
	bipush 99
	fastore
Label1:
	return
.limit stack 5
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
	bipush 100
	newarray float
	dup
	iconst_0
	iconst_2
	iastore
	dup
	iconst_1
	iconst_3
	iastore
	dup
	bipush 10
	iconst_1
	iastore
	dup
	bipush 20
	iconst_5
	iastore
	putstatic MT22Class.x [F
Label1:
	return
.limit stack 4
.limit locals 0
.end method
