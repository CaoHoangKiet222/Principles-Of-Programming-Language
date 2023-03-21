.source MT22Class.java
.class public MT22Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	ifgt Label3
	iconst_1
	goto Label2
Label3:
	iconst_0
Label2:
	invokestatic io/printBoolean(Z)V
	iconst_1
	ifgt Label5
	iconst_1
	goto Label4
Label5:
	iconst_0
Label4:
	invokestatic io/printBoolean(Z)V
	iconst_0
	ifgt Label7
	iconst_1
	goto Label6
Label7:
	iconst_0
Label6:
	ifgt Label9
	iconst_1
	goto Label8
Label9:
	iconst_0
Label8:
	invokestatic io/printBoolean(Z)V
	iconst_1
	ifgt Label11
	iconst_1
	goto Label10
Label11:
	iconst_0
Label10:
	ifgt Label13
	iconst_1
	goto Label12
Label13:
	iconst_0
Label12:
	invokestatic io/printBoolean(Z)V
	iconst_0
	ifgt Label15
	iconst_1
	goto Label14
Label15:
	iconst_0
Label14:
	ifgt Label17
	iconst_1
	goto Label16
Label17:
	iconst_0
Label16:
	ifgt Label19
	iconst_1
	goto Label18
Label19:
	iconst_0
Label18:
	invokestatic io/printBoolean(Z)V
	iconst_1
	ifgt Label21
	iconst_1
	goto Label20
Label21:
	iconst_0
Label20:
	ifgt Label23
	iconst_1
	goto Label22
Label23:
	iconst_0
Label22:
	ifgt Label25
	iconst_1
	goto Label24
Label25:
	iconst_0
Label24:
	invokestatic io/printBoolean(Z)V
	iconst_0
	ifgt Label27
	iconst_1
	goto Label26
Label27:
	iconst_0
Label26:
	iconst_1
	iand
	invokestatic io/printBoolean(Z)V
	iconst_1
	ifgt Label29
	iconst_1
	goto Label28
Label29:
	iconst_0
Label28:
	iconst_0
	iand
	invokestatic io/printBoolean(Z)V
	iconst_0
	ifgt Label31
	iconst_1
	goto Label30
Label31:
	iconst_0
Label30:
	ifgt Label33
	iconst_1
	goto Label32
Label33:
	iconst_0
Label32:
	iconst_1
	ifgt Label35
	iconst_1
	goto Label34
Label35:
	iconst_0
Label34:
	ifgt Label37
	iconst_1
	goto Label36
Label37:
	iconst_0
Label36:
	ifgt Label39
	iconst_1
	goto Label38
Label39:
	iconst_0
Label38:
	iand
	iconst_0
	ior
	iconst_1
	iand
	invokestatic io/printBoolean(Z)V
	iconst_1
	ifgt Label41
	iconst_1
	goto Label40
Label41:
	iconst_0
Label40:
	ifgt Label43
	iconst_1
	goto Label42
Label43:
	iconst_0
Label42:
	iconst_0
	ior
	invokestatic io/printBoolean(Z)V
Label1:
	return
.limit stack 81
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
