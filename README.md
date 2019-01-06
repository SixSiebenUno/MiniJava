# MiniJava

罗齐尧 15307130105

吴灵杰 15307130091



GitHub : https://github.com/SixSiebenUno/MiniJava



* 环境：

Mac OS / Ubuntu

Python 3

Antlr V4



* Python包：

Antlr4-Python3-runtime

graphviz



* 文件夹

```
---- MiniJava
 |-- readme.md
 |-- report.pdf
 |-- src (源代码)
 	|-- MiniJava.py
 	|-- ...
 	|-- tree.gv.png (输出的抽象语法树图片)
 |-- sample (测试数据集)
 	|-- factorial.java
 	|-- ...
```





* 运行指令：

```bash
$ cd src
$ python MiniJava.py ../sample/factorial.java [-AST] [-treegraph]

[-OPTIONS] :
	[-AST] 输出抽象语法树的字符串格式
	[-treegraph] 输出抽象语法树的图片形态
```



* 分工：

吴灵杰：文法文件（minijava.g4），利用antlr生成语法器和词法器，code review and debug

罗齐尧：完成语义错误处理，整合代码，实现可视化的抽象语法树输出，完成readme.md和报告

