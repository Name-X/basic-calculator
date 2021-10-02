class Parser:

    def parse(self, tokens):
        self.tokens = tokens
        self.movePointer()
        return self.evalExpr()

    def movePointer(self):
        if len(self.tokens):
            self.current = self.tokens.pop(0)
        else:
            self.current = None

    def performOperation(self, op, x, y):
        if op == '+':
            return x + y
        if op == '-':
            return x - y
        if op == '*':
            return x * y
        if op == '/':
            return x / y
        raise Exception('Unknown operator: ' + op)

    def evalExpr(self):
        result = self.constantNum()
        while self.current in ('+', '-', '*', '/'):
            op = self.current
            self.movePointer()
            leftNum = result
            rightNum = self.evalExpr()
            result = self.performOperation(op, leftNum, rightNum)
        return result

    def constantNum(self):
        if self.current == '-':
            self.movePointer()
            result = -(self.base())
        else:
            result = self.base()
        return result

    def base(self):
        result = None
        if type(self.current) is float:
            result = self.current
            self.movePointer()
        elif self.current == '(':
            self.movePointer()
            result = self.evalExpr()
            if self.current != ')':
                raise Exception('Expected )')
            self.movePointer()
        else:
            raise Exception('Expected number or (valid expression)')
        return result
