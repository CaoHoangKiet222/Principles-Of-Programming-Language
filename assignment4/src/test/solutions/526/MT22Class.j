.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static i I
.field static a [I
.field static b [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is c [I from Label0 to Label1
	bipush 10
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	astore_1
.var 2 is d [I from Label0 to Label1
	bipush 10
	newarray int
	dup
	iconst_0
	iconst_2
	iastore
	dup
	iconst_1
	iconst_3
	iastore
	dup
	iconst_2
	iconst_4
	iastore
	dup
	iconst_3
	iconst_5
	iastore
	astore_2
	getstatic MT22Class.a [I
	iconst_2
	iaload
	getstatic MT22Class.b [I
	iconst_1
	iaload
	iadd
	aload_1
	iconst_0
	iaload
	iadd
	aload_2
	iconst_5
	iaload
	iadd
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 17
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
	iconst_1
	putstatic MT22Class.i I
	bipush 10
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	putstatic MT22Class.a [I
	bipush 10
	newarray int
	putstatic MT22Class.b [I
Label1:
	return
.limit stack 9
.limit locals 0
.end method
