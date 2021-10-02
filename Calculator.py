from Compute import Compute
import utils.utils as utils

def run(inputExpr):
    cmp = Compute()
    isValid, statusMessage = utils.isValidExpr(inputExpr) 
    if isValid:
        tokenList, err = cmp.getTokens(inputExpr)
        if err=='':
            res = cmp.compute(tokenList)
            print(res, err)
            return round(res,2)
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