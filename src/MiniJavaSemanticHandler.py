from antlr4 import *
from MiniJavaVisitor import *
from MiniJavaListener import *


# the Visitor Implementation
class MyVisitor(MiniJavaVisitor):
    def __init__(self,*args,**kargs):
        #super(MyVisitor,self).__init__(self,*args,**kargs)
        #symbol = SymbolList()
        self.symbols = SymbolStack()
        print(1)
    def printerror(self,s,token):
        line = token.line
        column = token.column
        msg = s
        print ("line " + str(line) + ":"+str(column)+"\t"+"SematicFault "+ msg)

    def errorIdUnDec(self,s,ctx):
        self.printerror(s,ctx)
       # print s

    def errorMultipleDec(self,s,ctx):
        self.printerror(s,ctx)
       # print s

    def check(self,key):
        return self.symbols.check(key)

    # Expression Handling
    # new{}
    def visitStatparent(self, ctx):

        symbol = self.symbols.addNew()
        statname = ctx.Identifier(0).getText()
        ret = self.visitChildren(ctx)
        self.symbols.delLast()
        return ret 
    
    def visitStatdef(self, ctx):
        symbol = self.symbols.getTop()
        idname = ctx.Identifier().getText()
        if not self.check(idname):
            self.errorMultipleDec("Unknown Identifer: " + idname , ctx.Identifier().getSymbol())
        ret = self.visitChildren(ctx)
        return ret 
    # starting
    def visitGoal(self, ctx):
        print(333)
        symbol = self.symbols.addNew()
        print(777, ctx.getChildCount())
        ret = self.visitChildren(ctx)
        self.symbols.delLast()
        return ret
    # new{}
    def visitMainclass(self, ctx):
        prevsymbol = self.symbols.getTop()
        
        classname = ctx.Identifier(0).getText()
        if not self.check(classname):
            prevsymbol.push(classname,"mainclass")
        else:
            self.errorMultipleDec("Multiple Mainclass Dec: " + classname , ctx.Identifier(0).getSymbol())
        
        symbol = self.symbols.addNew()
        ret = self.visitChildren(ctx)
        self.symbols.delLast()
        return ret 

    def visitDecclass(self, ctx):
        prevsymbol = self.symbols.getTop()
        classname = ctx.Identifier(0).getText()
        if not self.check(classname):
            prevsymbol.push(classname,"class")
        else:
            self.errorMultipleDec("Multiple Class Dec: " \
                                  + classname,ctx.Identifier(0).getSymbol())
        symbol = self.symbols.addNew()
        ret = self.visitChildren(ctx)
        self.symbols.delLast()
        return ret 

    # Visit a parse tree produced by miniJavaParser#decvar.
    def visitDecvar(self, ctx):
        print(1)
        prevsymbol = self.symbols.getTop()
        varname = ctx.Identifier().getText()
        vartype = ctx.type0().getText()
        if self.check(varname) == False:
            prevsymbol.push(varname,vartype)
        else:
            self.errorMultipleDec("Multiple Vars Dec: " + varname,ctx.Identifier().getSymbol())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by miniJavaParser#decmethod.
    def visitDecmethod(self, ctx):
        prevsymbol = self.symbols.getTop()

        methodname = ctx.Identifier(0).getText()
        methodtype = ctx.type0(0).getText()
        

        if self.check(methodname) == False:
            prevsymbol.push(methodname,methodtype)
          
        # forgot there would be overide for the java class method
           # errorMultipleDec("Multiple Method Dec: " + methodname,ctx.Identifier(0).getSymbol())
        
        # adding the method vars
        symbol = self.symbols.addNew()
        try:
            for i in range(1,10):
              #  print i
                vartype = ctx.type0(i).getText()
                varname = ctx.Identifier(i).getText()
             #   print varname,vartype
                var = ctx.Identifier(i)
             #   print "b"
              #  print symbol
                #print self.symblos[-2].symbol
                if symbol.check(varname) == False:
                    symbol.push(varname,vartype)
                   # print "aaa"
                else:
                    self.errorMultipleDec("Multiple Vars Dec: " + varname,var.getSymbol())
        except:
            # here is the end
              pass

        ret = self.visitChildren(ctx)
        self.symbols.delLast()
        return ret 
    

    def visitId(self,ctx):
        Id = ctx.Identifier().getText()
        token = ctx.Identifier().getSymbol()
        a = self.check(Id)
        if  a == False:
            self.errorIdUnDec("Unknown Identifer: "+ Id,ctx.Identifier().getSymbol())
        return a


class SymbolStack(object):
    def __init__(self,*args,**kargs):
        self.symbols = {}
        self.stack = []
        self.history = []
        print(111)
    def printStack(self):
        for i in self.stack:
            print (i.symbols)

    def check(self,key):
        res = None
        for i in self.stack:
            try:
                res = i.symbols[key]
            except:
                continue
      #  print res
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
        #print self.stack
        last = self.stack.pop()
        self.history.append("POP")
        return last

class SymbolList(object):
    def __init__(self,*args,**kargs):
        self.symbols = {}
        print(222)
    def push(self,key,value):
        try:
            self.symbols[key] = value
        except:
            print ("symbollist push error")
    def pop(self,key):
        try:
            self.symbols.pop(key)
        except:
            print ("pop error")
    def check(self,key):
        try:
            ret = self.symbols[key]
        except:
            ret = False
        return ret
