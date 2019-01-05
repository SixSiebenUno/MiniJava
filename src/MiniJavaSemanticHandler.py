from antlr4 import *
from MiniJavaVisitor import *
from MiniJavaListener import *


def PrintDetail(token, line, column):
    input = token.getInputStream()
    string = str(input).split('\n')[line - 1]
    print(string)

    underline = ''
    idx = 0
    for char in string:
        if char == '\t':
            underline += '\t'
            idx += 1
        else:
            break
    for i in range(idx, column):
        if string[i] == '\t':
            underline += '\t'
        else:
            underline += ' '
    underline += '^'
    print(underline)


class MyVisitor(MiniJavaVisitor):
    def __init__(self,*args,**kargs):
        self.symbols = SymbolStack()
    
    def printerror(self,s,token):
        line = token.line
        column = token.column
        msg = s
        print ("line " + str(line) + ":"+str(column)+"\t"+"SemanticFault "+ msg)
        PrintDetail(token, line, column)

    def errorIdUnDec(self,s,ctx):
        self.printerror(s,ctx)

    def errorMultipleDec(self,s,ctx):
        self.printerror(s,ctx)

    def check(self,key):
        return self.symbols.check(key)
    
    def visitStatement(self, ctx):
        # print("state def")
        symbol = self.symbols.getTop()
        # print(ctx.Identifier())
        # print(symbol)
        if ctx.Identifier() == None:
            return
        idname = ctx.Identifier().getText()
        # print ("visitStatdef: ", symbol, idname)
        if not self.check(idname):
            self.errorMultipleDec("Unknown Identifer: " + idname , ctx.Identifier().getSymbol())
        ret = self.visitChildren(ctx)
        return ret 

    def visitGoal(self, ctx):
        symbol = self.symbols.addNew()
        ret = self.visitChildren(ctx)
        self.symbols.delLast()
        return ret
        
    def visitMainClassDeclaration(self, ctx):
        prevsymbol = self.symbols.getTop()
        
        classname = ctx.Identifier().getText()
        if not self.check(classname):
            prevsymbol.push(classname,"mainclass")
        else:
            self.errorMultipleDec("Multiple Mainclass Dec: " + classname , ctx.Identifier(0).getSymbol())
        symbol = self.symbols.addNew()
        ret = self.visitChildren(ctx)
        self.symbols.delLast()
        return ret 

    def visitClassDeclaration(self, ctx):
        prevsymbol = self.symbols.getTop()
        classname = ctx.Identifier().getText()
        if not self.check(classname):
            prevsymbol.push(classname,"class")
        else:
            self.errorMultipleDec("Multiple Class Dec: " + classname,ctx.Identifier().getSymbol())
        symbol = self.symbols.addNew()
        ret = self.visitChildren(ctx)
        self.symbols.delLast()
        return ret 

    def visitVarDeclaration(self, ctx):
        prevsymbol = self.symbols.getTop()
        varname = ctx.Identifier().getText()
        vartype = ctx.valueType().getText()
        if self.check(varname) == False:
            prevsymbol.push(varname,vartype)
        else:
            self.errorMultipleDec("Multiple Varations Dec: " + varname,ctx.Identifier().getSymbol())
        return self.visitChildren(ctx)

    def visitMethodDeclaration(self, ctx):
        prevsymbol = self.symbols.getTop()
        methodname = ctx.Identifier().getText()
        methodtype = ctx.valueType().getText()
        # print("*** method" , methodname, methodtype)
        if self.check(methodname) == False:
            prevsymbol.push(methodname, methodtype)
        symbol = self.symbols.addNew()
        try:
            # print(ctx.valueType(), ctx.Identifier())
            for i in range(1,10):
                vartype = ctx.valueType(i).getText()
                varname = ctx.Identifier(i).getText()
                var = ctx.Identifier(i)
                # print("add var ", vartype, varname)
                if symbol.check(varname) == False:
                    symbol.push(varname,vartype)
                else:
                    self.errorMultipleDec("Multiple Varations Dec: " + varname,var.getSymbol())
        except:
              pass

        ret = self.visitChildren(ctx)
        self.symbols.delLast()
        return ret 

    def visitParameter(self,ctx):
        Id = ctx.Identifier().getText()
        # print ("visit id " , Id, self.check(Id))
        a = self.check(Id)
        if  a == False:
            pass
            # self.errorIdUnDec("Unknown Identifer: "+ Id,ctx.Identifier().getSymbol())
        return a


class SymbolStack(object):
    def __init__(self,*args,**kargs):
        self.symbols = {}
        self.stack = []
        self.history = []

    def printStack(self):
        for i in self.stack:
            print (i.symbols)

    def check(self,key):
        res = None
        for i in self.stack:
            try:
                res = i.symbols[key]
            except: continue
        if res == None:
            return False
        else:
            return res

    def addNew(self):
        a = SymbolList()
        self.stack.append(a)
        self.history.append(a)
        return a

    def getTop(self):
        return self.stack[-1]

    def delLast(self):
        last = self.stack.pop()
        self.history.append("POP")
        return last


class SymbolList(object):
    def __init__(self,*args,**kargs):
        self.symbols = {}

    def push(self,key,value):
        self.symbols[key] = value

    def pop(self,key):
        self.symbols.pop(key)

    def check(self,key):
        try:
            ret = self.symbols[key]
        except:
            ret = False
        return ret
