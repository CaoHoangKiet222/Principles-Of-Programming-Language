.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	ifgt Label3
	iconst_1
	goto Label2
Label3:
	iconst_0
Label2:
	invokestatic io/printBoolean(Z)V
	iconst_1
	iconst_0
	iand
	ifgt Label5
	iconst_1
	goto Label4
Label5:
	iconst_0
Label4:
	invokestatic io/printBoolean(Z)V
Label1:
	return
.limit stack 10
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
