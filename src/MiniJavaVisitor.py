# Generated from .\MiniJava.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniJavaParser import MiniJavaParser
else:
    from MiniJavaParser import MiniJavaParser

# This class defines a complete generic visitor for a parse tree produced by MiniJavaParser.

class MiniJavaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniJavaParser#goal.
    def visitGoal(self, ctx:MiniJavaParser.GoalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#mainClassDeclaration.
    def visitMainClassDeclaration(self, ctx:MiniJavaParser.MainClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#mainClassBody.
    def visitMainClassBody(self, ctx:MiniJavaParser.MainClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#mainMethod.
    def visitMainMethod(self, ctx:MiniJavaParser.MainMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#mainMethodDeclaration.
    def visitMainMethodDeclaration(self, ctx:MiniJavaParser.MainMethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#classDeclaration.
    def visitClassDeclaration(self, ctx:MiniJavaParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#classBody.
    def visitClassBody(self, ctx:MiniJavaParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#varDeclaration.
    def visitVarDeclaration(self, ctx:MiniJavaParser.VarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:MiniJavaParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#methodBody.
    def visitMethodBody(self, ctx:MiniJavaParser.MethodBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#parameters.
    def visitParameters(self, ctx:MiniJavaParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#parameterList.
    def visitParameterList(self, ctx:MiniJavaParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#parameter.
    def visitParameter(self, ctx:MiniJavaParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#valueType.
    def visitValueType(self, ctx:MiniJavaParser.ValueTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#statement.
    def visitStatement(self, ctx:MiniJavaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#expression.
    def visitExpression(self, ctx:MiniJavaParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#intArrayType.
    def visitIntArrayType(self, ctx:MiniJavaParser.IntArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#boolType.
    def visitBoolType(self, ctx:MiniJavaParser.BoolTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniJavaParser#intType.
    def visitIntType(self, ctx:MiniJavaParser.IntTypeContext):
        return self.visitChildren(ctx)



del MiniJavaParser