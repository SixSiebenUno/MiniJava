from antlr4 import FileStream, CommonTokenStream, tree
from MiniJavaLexer import MiniJavaLexer
from MiniJavaParser import MiniJavaParser
from MiniJavaVisitor import MiniJavaVisitor
from MiniJavaErrorHandler import MiniJavaErrorListener
from MiniJavaSemanticHandler import *
from antlr4.tree.Trees import Trees
from graphviz import Digraph
import argparse
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

    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='input_file')
    parser.add_argument('-AST', '--ast_flag',
                        action='store_true', default=False, help="ast_flag")
    parser.add_argument('-treegraph', '--tree_flag',
                        action='store_true', default=False, help="tree_flag")
    args = parser.parse_args()

    if args.input is None:
        print("Instruction Error!")
        print("Usage : python MiniJava.py demo.java [-AST -treegraph]")
    
    input = FileStream(args.input)

    print("------------------------")
    print("Lexical and Syntax Check...")

    lexer = MiniJavaLexer(input)
    stream = CommonTokenStream(lexer)
    parser = MiniJavaParser(stream)

    print("Lexical and Syntax Check Done.")

    #parser.removeErrorListeners()
    #parser.addErrorListener(MiniJavaErrorListener())
    tree = parser.goal()

    print("------------------------")
    print("Semantic Check...")
    
    visitor = MyVisitor()
    visitor.visit(tree)

    print("Semantic Check Done.")
    print("------------------------")
    if args.ast_flag:
        print("AST string:")
        print(Trees.toStringTree(tree, None, parser))
        print("------------------------")

    if args.tree_flag:
        print("Generate Parse Tree...")
        DFS(tree, 0, "")
        dot.format = 'png'
        dot.render('tree.gv', view=True)
        print("Generate Parse Tree Finished.")


if __name__ == "__main__":
    main()
    
