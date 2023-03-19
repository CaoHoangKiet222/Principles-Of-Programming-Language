.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static less_zero Z
.field static c I

.method public static printPattern(I)V
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	goto Label5
Label4:
	iconst_1
	putstatic MT22Class.less_zero Z
Label5:
	getstatic MT22Class.less_zero Z
	ifgt Label6
	getstatic MT22Class.c I
	iconst_1
	iadd
	putstatic MT22Class.c I
	iload_0
	iconst_5
	isub
	invokestatic MT22Class/printPattern(I)V
	goto Label7
Label6:
	getstatic MT22Class.c I
	iconst_1
	isub
	putstatic MT22Class.c I
	getstatic MT22Class.c I
	iconst_1
	ineg
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	goto Label11
Label10:
	iload_0
	invokestatic io/printInteger(I)V
	return
Label11:
	iload_0
	iconst_5
	iadd
	invokestatic MT22Class/printPattern(I)V
Label7:
Label1:
	return
.limit stack 7
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
	invokestatic MT22Class/printPattern(I)V
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
	iconst_0
	putstatic MT22Class.less_zero Z
	iconst_0
	putstatic MT22Class.c I
Label1:
	return
.limit stack 3
.limit locals 0
.end method
