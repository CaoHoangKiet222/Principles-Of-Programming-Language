.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	ineg
	ineg
	invokestatic io/printInteger(I)V
	bipush 100
	ineg
	ineg
	invokestatic io/printInteger(I)V
	ldc 1.0
	fneg
	fneg
	invokestatic io/writeFloat(F)V
	ldc 10000.0
	fneg
	fneg
	invokestatic io/writeFloat(F)V
	iconst_1
	ineg
	ineg
	ineg
	invokestatic io/printInteger(I)V
	bipush 100
	ineg
	ineg
	ineg
	invokestatic io/printInteger(I)V
	ldc 1.0
	fneg
	fneg
	fneg
	invokestatic io/writeFloat(F)V
	ldc 10000.0
	fneg
	fneg
	fneg
	invokestatic io/writeFloat(F)V
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
