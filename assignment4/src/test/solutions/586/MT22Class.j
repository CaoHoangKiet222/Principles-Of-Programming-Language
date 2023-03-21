.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static findMin([II)I
.var 0 is vals [I from Label0 to Label1
.var 1 is numEls I from Label0 to Label1
Label0:
.var 2 is min I from Label0 to Label1
	aload_0
	iconst_0
	iaload
	istore_2
.var 3 is i I from Label0 to Label1
	iconst_1
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
	ifle Label3
Label8:
	aload_0
	iload_3
	iaload
	iload_2
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
	goto Label13
Label12:
	aload_0
	iload_3
	iaload
	istore_2
Label13:
Label9:
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
.limit stack 9
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is arr [I from Label0 to Label1
	bipush 10
	newarray int
	dup
	iconst_0
	bipush 10
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
.var 2 is n I from Label0 to Label1
	bipush 10
	istore_2
	aload_1
	iload_2
	invokestatic MT22Class/findMin([II)I
	invokestatic io/printInteger(I)V
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
