from antlr4 import FileStream, CommonTokenStream, tree
from MiniJavaLexer import MiniJavaLexer
from MiniJavaParser import MiniJavaParser
from MiniJavaVisitor import MiniJavaVisitor
from antlr4.tree.Trees import Trees
import sys


def DFS(node, prefix_str):
    if isinstance(node, tree.Tree.TerminalNode):
        print(prefix_str + node.getText())
        return
    for child in node.getChildren():
        DFS(child, prefix_str + "\t")


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
    DFS(tree, "")


if __name__ == "__main__":
    main()
    