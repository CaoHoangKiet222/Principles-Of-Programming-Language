.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 100
	bipush 20
	isub
	invokestatic io/printInteger(I)V
	ldc 100.0
	bipush 20
	i2f
	fsub
	invokestatic io/writeFloat(F)V
	bipush 100
	i2f
	ldc 20.0
	fsub
	invokestatic io/writeFloat(F)V
	ldc 100.0
	ldc 20.0
	fsub
	invokestatic io/writeFloat(F)V
Label1:
	return
.limit stack 6
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
