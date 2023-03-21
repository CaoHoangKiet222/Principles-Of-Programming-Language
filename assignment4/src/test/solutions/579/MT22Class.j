.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static count(I)Z
.var 0 is n I from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
.var 2 is c I from Label0 to Label1
	iconst_0
	istore_2
	iconst_1
	istore_1
Label2:
	iload_1
	iload_0
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
	iload_0
	iload_1
	irem
	iconst_0
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	goto Label11
Label10:
	iload_2
	iconst_1
	iadd
	istore_2
Label11:
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label5:
	iload_2
	iconst_2
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	iconst_0
	ireturn
Label14:
	iconst_1
	ireturn
Label15:
Label1:
.limit stack 9
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n I from Label0 to Label1
	bipush 10
	istore_1
	iload_1
	invokestatic MT22Class/count(I)Z
	iconst_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	ldc "n is not prime number"
	invokestatic io/printString(Ljava/lang/String;)V
	goto Label5
Label4:
	ldc "n is prime number"
	invokestatic io/printString(Ljava/lang/String;)V
Label5:
Label1:
	return
.limit stack 4
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
