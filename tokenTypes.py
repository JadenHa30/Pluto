TOKEN_OPERATOR_TYPES = [
    (r"=", "ASSIGN"),
    (r"\*=", "MUL_ASSIGN"),
    (r"/=", "DIV_ASSIGN"),
    (r"%=", "MOD_ASSIGN"),
    (r"\+=", "ADD_ASSIGN"),
    (r"-=", "SUB_ASSIGN"),
    (r"<<=", "LEFT_SHIFT_ASSIGN"),
    (r">>=", "RIGHT_SHIFT_ASSIGN"),
    (r"&=", "AND_ASSIGN"),
    (r"\^=", "XOR_ASSIGN"),
    (r"\|=", "OR_ASSIGN"),

    (r">", "GREATER_THAN"),
    (r"<", "LESS_THAN"),
    (r"<<", "LEFT_SHIFT"),
    (r">>", "RIGHT_SHIFT"),
    (r"\|\|", "LOGICAL_OR"),
    (r"&&", "LOGICAL_AND"),

    (r"&", "ADDRESS_OF"),
    (r"\*", "DEREFERENCE"),

    (r"\+", "UNARY_PLUS"),
    (r"-", "UNARY_MINUS"),
    (r"~", "BITWISE_NOT"),
    (r"!", "LOGICAL_NOT"),
    
    (r"\?", "TERNARY_QUESTION"),
    (r":", "TERNARY_COLON"),
]

TOKEN_TYPES = [
    (r'\b(loop|enum|hmm|else|hmm\?)\b', 'KEYWORD'),
    (r'<<<<', 'END_BLOCK'),
    (r'\b[A-Za-z_][A-Za-z0-9_]*\b', 'IDENTIFIER'),
    (r'"[^"]+"', 'STRING'),
    (r'[+-]?([0-9]+[.][0-9]*|[.][0-9]+)([eE][+-]?[0-9]+)?f?', 'FLOAT'),
    (r'\d+', 'INTEGER'),
    (r'[():]', 'SYMBOL'),
    (r'//', None),  # Ignore comments
    (r'/\*[^*]*\*+(?:[^/*][^*]*\*+)*/', None), #Block comments
    (r'\s+', None),  # Ignore whitespace
]

TOKEN_TYPES.extend(TOKEN_OPERATOR_TYPES)
