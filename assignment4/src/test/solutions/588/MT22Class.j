.source MT22Class.java
.class public MT22Class
.super java.lang.Object
.field static a I
.field static b I
.field static c I
.field static y I
.field static z I
.field static x [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label2:
	iload_1
	bipush 100
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label3
Label8:
	getstatic MT22Class.b I
	getstatic MT22Class.c I
	iadd
	putstatic MT22Class.a I
	getstatic MT22Class.x [I
	iconst_0
	bipush 100
	imul
	iload_1
	iadd
	getstatic MT22Class.y I
	getstatic MT22Class.z I
	irem
	iastore
Label9:
Label4:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label2
Label3:
Label5:
	getstatic MT22Class.a I
	invokestatic io/printInteger(I)V
	getstatic MT22Class.x [I
	iconst_0
	bipush 100
	imul
	iconst_1
	iadd
	iaload
	invokestatic io/printInteger(I)V
Label1:
	return
.limit stack 8
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
	iconst_1
	ineg
	putstatic MT22Class.a I
	iconst_0
	putstatic MT22Class.b I
	iconst_3
	putstatic MT22Class.c I
	iconst_1
	putstatic MT22Class.y I
	iconst_1
	putstatic MT22Class.z I
	bipush 100
	newarray int
	putstatic MT22Class.x [I
Label1:
	return
.limit stack 5
.limit locals 0
.end method
