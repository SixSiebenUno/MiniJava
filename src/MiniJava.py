from antlr4 import FileStream, CommonTokenStream, tree
from MiniJavaLexer import MiniJavaLexer
from MiniJavaParser import MiniJavaParser
from MiniJavaVisitor import MiniJavaVisitor
from antlr4.tree.Trees import Trees
from graphviz import Digraph
import sys

cnt = 0
ruleNames =  [ "goal", "mainClassDeclaration", "mainClassBody", "mainMethod", 
                "mainMethodDeclaration", "classDeclaration", "classBody", 
                "varDeclaration", "methodDeclaration", "methodBody", 
                "parameters", "parameterList", "parameter", "valueType", 
                "statement", "expression", "intArrayType", "boolType", 
                "intType" ]

def DFS(node, fa, prefix_str):
    global cnt
    cnt += 1
    idx = cnt
    if isinstance(node, tree.Tree.TerminalNode):
        dot.node(str(idx), str(node.getText()))
    else:
        dot.node(str(idx), ruleNames[node.getRuleIndex()])
    if fa != 0:
        dot.edge(str(fa), str(idx))
    if isinstance(node, tree.Tree.TerminalNode):
        print(prefix_str + node.getText())
        return
    for child in node.getChildren():
        DFS(child, idx, prefix_str + "\t")


def main():
    if len(sys.argv) != 2:
        print ("Instruction Error!")
        print ("Usage : python MiniJava.py demo.java")
        return
    input = FileStream(sys.argv[1])
    lexer = MiniJavaLexer(input)
    stream = CommonTokenStream(lexer)
    parser = MiniJavaParser(stream)
    tree = parser.goal()
    print(Trees.toStringTree(tree, None, parser))
    DFS(tree, 0, "")


if __name__ == "__main__":
    dot = Digraph(comment='Tree')
    main()
    dot.format = 'png'
    dot.render('tree.gv', view=True)
    