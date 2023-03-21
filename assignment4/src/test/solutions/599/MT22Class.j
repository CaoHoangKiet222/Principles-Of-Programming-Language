.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static haha(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iconst_1
	ireturn
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static haha1()F
Label0:
.var 0 is x I from Label0 to Label1
	bipush 100
	istore_0
	iconst_1
	i2f
	freturn
Label1:
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is x I from Label0 to Label1
	bipush 100
	istore_1
	iload_1
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
