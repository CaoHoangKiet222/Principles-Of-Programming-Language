.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static foo1(Ljava/lang/String;F)Ljava/lang/String;
.var 0 is c Ljava/lang/String; from Label0 to Label1
.var 1 is d F from Label0 to Label1
Label0:
	ldc "foo1"
	areturn
Label1:
.limit stack 1
.limit locals 2
.end method

.method public static foo(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;
.var 0 is a Ljava/lang/String; from Label0 to Label1
.var 1 is b Ljava/lang/String; from Label0 to Label1
Label0:
.var 2 is d F from Label0 to Label1
	ldc 123.0
	fstore_2
.var 3 is c Ljava/lang/String; from Label0 to Label1
	ldc "World!"
	aload_1
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore_3
	ldc "foo"
	areturn
Label1:
.limit stack 4
.limit locals 4
.end method

.method public static bar(ILjava/lang/String;)V
.var 0 is x I from Label0 to Label1
.var 1 is y Ljava/lang/String; from Label0 to Label1
Label0:
.var 2 is b Ljava/lang/String; from Label0 to Label1
	ldc "Kiet"
	astore_2
.var 3 is a Ljava/lang/String; from Label0 to Label1
	ldc "Hello"
	astore_3
.var 4 is d F from Label0 to Label1
	ldc 123.0
	fstore 4
.var 5 is c Ljava/lang/String; from Label0 to Label1
	ldc "World!"
	aload_2
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	astore 5
.var 6 is b I from Label0 to Label1
	iconst_3
	istore 6
	aload_3
	aload 5
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	ldc "\n"
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	invokestatic io/printString(Ljava/lang/String;)V
	iload 6
	iload_0
	iadd
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 4
.limit locals 7
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
