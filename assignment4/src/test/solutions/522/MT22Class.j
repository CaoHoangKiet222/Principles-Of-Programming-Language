.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_2
	iconst_1
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iconst_3
	iand
	iconst_4
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/printBoolean(Z)V
	ldc 2.0
	iconst_1
	i2f
	fcmpl
	ifle Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iconst_3
	iand
	iconst_4
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	invokestatic io/printBoolean(Z)V
Label1:
	return
.limit stack 16
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
