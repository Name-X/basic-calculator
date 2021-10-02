import utils.utils as utils
from Compute import Compute

def run(inputExpr):
    isValid, statusMessage = utils.isValidExpr(inputExpr) 
    print(isValid, statusMessage)
    if isValid:
        cmp = Compute()
        tokenList, err = cmp.getTokens(inputExpr)
        if err=='':
            print(tokenList)
        else:
            print("Error while tokenizing ", err)
            return None
    else:
        print(statusMessage)
        return None
    return None
   
if __name__ == '__main__':
    inputExpr = input("Enter the expression to be evaluated:  ")
    inputExpr = inputExpr.replace(" ","")
    if inputExpr =='':
        print("Empty expression exiting")
    else:
        run(inputExpr)