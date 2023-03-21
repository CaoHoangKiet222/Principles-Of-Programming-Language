.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static foo(Ljava/lang/String;F)Ljava/lang/String;
.var 0 is a Ljava/lang/String; from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
.var 2 is d Ljava/lang/String; from Label0 to Label1
	aload_0
	astore_2
.var 3 is f [Ljava/lang/String; from Label0 to Label1
	iconst_5
	anewarray java/lang/String
	dup
	iconst_0
	ldc "Yooooo!"
	aastore
	dup
	iconst_1
	ldc "Loooo"
	aastore
	astore_3
	aload_3
	iconst_0
	aaload
	aload_3
	iconst_1
	aaload
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	aload_2
	invokevirtual java/lang/String/concat(Ljava/lang/String;)Ljava/lang/String;
	areturn
Label1:
.limit stack 6
.limit locals 4
.end method

.method public static bar(FLjava/lang/String;)V
.var 0 is a F from Label0 to Label1
.var 1 is b Ljava/lang/String; from Label0 to Label1
Label0:
.var 2 is b F from Label0 to Label1
	bipush 123
	i2f
	fstore_2
.var 3 is a Ljava/lang/String; from Label0 to Label1
	ldc "Hello"
	astore_3
.var 4 is i I from Label0 to Label1
	iconst_1
	istore 4
Label2:
	iload 4
	bipush 10
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
Label8:
	fload_0
	invokestatic io/writeFloat(F)V
Label9:
Label4:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label2
Label3:
Label5:
	fload_0
	iconst_2
	i2f
	fcmpl
	ifne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
	goto Label13
Label12:
	return
Label13:
Label1:
	return
.limit stack 7
.limit locals 5
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	i2f
	ldc "yep"
	invokestatic MT22Class/bar(FLjava/lang/String;)V
	ldc "Friend"
	iconst_1
	i2f
	invokestatic MT22Class/foo(Ljava/lang/String;F)Ljava/lang/String;
	invokestatic io/printString(Ljava/lang/String;)V
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
