grammar MiniJava;

goal
    :   mainClassDeclaration
        classDeclaration*
        EOF
    ;

mainClassDeclaration
    :   'class' Identifier
        mainClassBody
    ;

mainClassBody
    :   '{' mainMethod '}'
    ;

mainMethod
    :   mainMethodDeclaration '{' statement '}'
    ;

mainMethodDeclaration
    :   'public' 'static' 'void' 'main' '(' 'String' '[' ']' Identifier ')'
    ;

classDeclaration
    :   'class' Identifier ('extands' valueType)?
        classBody
    ;

classBody
    :   '{' varDeclaration*
            methodDeclaration* '}'
    ;

varDeclaration
    :   valueType Identifier ';'
    ;

methodDeclaration
    :   'public' valueType Identifier parameters
        methodBody
    ;

methodBody
    :   '{' varDeclaration*
            statement*
            'return' expression ';'
        '}'
    ;

parameters
    :   '(' parameterList? ')'
    ;

parameterList
    :   parameter (',' parameter)*
    ;

parameter
    :   valueType Identifier
    ;

valueType
    :   intArrayType
    |   boolType
    |   intType
    |   Identifier
    ;

statement
    :   '{' statement* '}'
    |   'if' '(' expression ')'
            statement
        'else'
            statement
    |   'while' '(' expression ')'
            statement
    |   'System.out.println' '(' expression ')' ';'
    |   Identifier '=' expression ';'
    |   Identifier '[' expression ']' '=' expression ';'
    ;

expression
    :   expression '&&' expression
    |   expression '<' expression
    |   expression '+' expression
    |   expression '-' expression
    |   expression '*' expression
    |   expression '[' expression ']'
    |   expression '.' 'length'
    |   expression '.' Identifier '(' (expression (',' expression)*)? ')'
    |   INT
    |   'true'
    |   'false'
    |   Identifier
    |   'this'
    |   'new' 'int' '[' expression ']'
    |   'new' Identifier '(' ')'
    |   '!' expression
    |   '(' expression ')'
    ;

intArrayType
    :   'int' '[' ']'
    ;

boolType
    :   'boolean'
    ;

intType
    :   'int'
    ;

INT
    :   ('0' | [1-9][0-9]*)
    ;

Identifier
    :   [a-zA-Z_][0-9a-zA-Z_]*
    ;

WS
    :   [ \r\t\n]+ -> skip
    ;

COMMENT
    :   '/*' .*? '*/' -> skip
    ;

LINE_COMMENT
    :   '//' ~[\r\n]* -> skip
    ;