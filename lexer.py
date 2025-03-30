import re
from tokenTypes import TOKEN_TYPES

def tokenize(code):
    tokens = []
    while code:
        for pattern, token_type in TOKEN_TYPES:
            match = re.match(pattern, code)
            if match:
                if token_type:
                    tokens.append((token_type, match.group(0)))
                code = code[len(match.group(0)):] #slice the string from index len(match.group(0)) onward
                print(code[len(match.group(0)):]) 
                break
        else:
            raise SyntaxError(f"Unexpected character: {code[0]}")
    return tokens

# Example usage
code = """
num = 42
message = "Hello, world!"

printSomething():
    return "Hello"
<<<<

hmm (num > 10):
    print("Greater than 10")
else
    print("10 or less")
<<<<
"""

test = tokenize(code)
for token in test:
    print(token)