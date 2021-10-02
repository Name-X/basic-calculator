from typing import List, Tuple

class Compute:

    OPERATORS = ['+', '-', '*', '/', '(', ')']

    def __init__(self):
        pass

    def getTokens(self, string:str) -> tuple:
        chars = list(string)
        tokens = []
        pos = 0
        errMessage = ''
        charLen = len(chars)
        while pos < charLen:
            i = chars[pos]
            if i in self.OPERATORS:
                tokens.append(i)
            else:
                num = float(i)
                while pos + 1 < len(chars) and chars[pos + 1].isdigit():
                    pos += 1
                    num = num * 10 + float(chars[pos])
                tokens.append(num)
            pos += 1
        return (tokens, errMessage)