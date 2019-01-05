from antlr4.error.ErrorListener import *

class MiniJavaErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("line " + str(line) + ":" + str(column) + " " + msg)
        self.MyPrintDetail(recognizer, offendingSymbol, line, column, msg, e)

    def MyPrintDetail(self, recognizer, offendingSymbol, line, column, msg, e):
        token = recognizer.getCurrentToken()
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
        for i in range(offendingSymbol.column - 1):
            if string[i + idx] == '\t':
                underline += '\t'
            else:
                underline += ''
        underline += '^'
        print(underline)


