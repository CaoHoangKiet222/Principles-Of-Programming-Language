.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static checkzero([II)Z
.var 0 is nums [I from Label0 to Label1
.var 1 is size I from Label0 to Label1
Label0:
.var 2 is found Z from Label0 to Label1
	iconst_0
	istore_2
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
Label2:
	iload_3
	iload_1
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iload_2
	ifgt Label9
	iconst_1
	goto Label8
Label9:
	iconst_0
Label8:
	iand
	ifle Label3
Label10:
	aload_0
	iload_3
	iaload
	iconst_0
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	goto Label15
Label14:
	iconst_1
	istore_2
Label15:
Label11:
Label4:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label2
Label3:
Label5:
	iload_2
	ireturn
Label1:
.limit stack 12
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n I from Label0 to Label1
	iconst_5
	istore_1
.var 2 is arr [I from Label0 to Label1
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	bipush 31
	iastore
	dup
	iconst_2
	bipush 23
	iastore
	dup
	iconst_3
	sipush 4324
	iastore
	dup
	iconst_4
	sipush 234
	iastore
	astore_2
	aload_2
	iload_1
	invokestatic MT22Class/checkzero([II)Z
	ifgt Label2
	ldc "zero doesn't contain in arr"
	invokestatic io/printString(Ljava/lang/String;)V
	goto Label3
Label2:
	ldc "arr has a zero"
	invokestatic io/printString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 4
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
