from typing import Tuple

_invalid_expr_message = 'Invalid expression paranthesis not matching'
def isParenthesisMatching(input:str)-> bool:
    stack = []
    input = input.replace(" ","")
    isValid = True
    errMessage = ''
    for i in input:
        if i == "(":
            stack.append("(")
        elif i == ")":
            if not stack:
                isValid = False
                errMessage = _invalid_expr_message 
                break
            popped = stack.pop()
            if popped == '(' and i != ')':
                isValid = False
                errMessage = _invalid_expr_message
                break
    if stack:
        errMessage = _invalid_expr_message
        return False, errMessage
    return isValid, errMessage

def isValidIdentifiers(input: str) -> Tuple[bool,str]:
    input = input.replace(" ","")
    isValid = True
    errMessage = ''
    for i in input:
        if i not in ["0", "1", "2", "3" , "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", ".", "(", ")"]:
            isValid = False
            errMessage = "Invalid character " +  i
            break
    return isValid, errMessage

def isValidExpr(input: str) -> Tuple[bool, str]:
    idCheck, msg = isValidIdentifiers(input)
    if (idCheck):
        return isParenthesisMatching(input)
    else:
        return idCheck, msg