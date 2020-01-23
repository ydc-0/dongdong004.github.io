class Operation(object):
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    
    def GetResult(self):
        # 子类重写
        return 0


class OperationAdd(Operation):
    def GetResult(self):
        return self.number1 + self.number2


class OperationSub(Operation):
    def GetResult(self):
        return self.number1 - self.number2


class OperationMul(Operation):
    def GetResult(self):
        return self.number1 * self.number2


class OperationDiv(Operation):
    def GetResult(self):
        return self.number1 / self.number2


class OperationFactory(object):
    pass