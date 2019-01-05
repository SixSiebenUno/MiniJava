from antlr4 import FileStream, CommonTokenStream, tree
from MiniJavaLexer import MiniJavaLexer
from MiniJavaParser import MiniJavaParser
from MiniJavaVisitor import MiniJavaVisitor
from MiniJavaErrorHandler import MiniJavaErrorListener
from MiniJavaSemanticHandler import *
from antlr4.tree.Trees import Trees
from graphviz import Digraph
import sys

cnt = 0
dot = Digraph(comment='Tree')

def DFS(node, fa, prefix_str):
    global cnt
    cnt += 1
    idx = cnt
    if isinstance(node, tree.Tree.TerminalNode):
        dot.node(str(idx), str(node.getText()))
    else:
        dot.node(str(idx), MiniJavaParser.ruleNames[node.getRuleIndex()])
    if fa != 0:
        dot.edge(str(fa), str(idx))
    if isinstance(node, tree.Tree.TerminalNode):
        # print(prefix_str + node.getText())
        return
    for child in node.getChildren():
        DFS(child, idx, prefix_str + "\t")


def main():
    if len(sys.argv) != 2:
        print ("Instruction Error!")
        print ("Usage : python MiniJava.py demo.java")
    
    input = FileStream(sys.argv[1])

    print ("------------------------")
    print ("Lexical and Syntax Check...")

    lexer = MiniJavaLexer(input)
    stream = CommonTokenStream(lexer)
    parser = MiniJavaParser(stream)

    #parser.removeErrorListeners()
    #parser.addErrorListener(MiniJavaErrorListener())
    tree = parser.goal()
    
    print ("------------------------")
    print ("Semantic Check...")
    
    visitor = MyVisitor()
    visitor.visit(tree)

    print ("------------------------")
    print(Trees.toStringTree(tree, None, parser))

    print ("------------------------")
    
    print ("Generate Parse Tree...")
    DFS(tree, 0, "")

    #dot.format = 'png'
    #dot.render('tree.gv', view=True)


if __name__ == "__main__":
    main()
    