import utils.utils as utils

def run(inputExpr):
    isValid, statusMessage = utils.isValidExpr(inputExpr) 
    print(isValid, statusMessage)
    return None
   
if __name__ == '__main__':
    inputExpr = input("Enter the expression to be evaluated:  ")
    inputExpr = inputExpr.replace(" ","")
    if inputExpr =='':
        print("Empty expression exiting")
    else:
        run(inputExpr)