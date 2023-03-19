.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static foo(Ljava/lang/String;F)Ljava/lang/String;
.var 0 is a Ljava/lang/String; from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
	ldc "foo"
	areturn
Label1:
.limit stack 1
.limit locals 2
.end method

.method public static bar(ILjava/lang/String;)V
.var 0 is x I from Label0 to Label1
.var 1 is y Ljava/lang/String; from Label0 to Label1
Label0:
Label1:
	return
.limit stack 0
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	ldc "hello"
	invokestatic MT22Class/bar(ILjava/lang/String;)V
Label1:
	return
.limit stack 2
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
