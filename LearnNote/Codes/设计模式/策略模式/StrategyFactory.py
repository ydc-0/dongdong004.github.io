# -*- coding: utf-8 -*-
from Strategy import Strategy
from Strategy import ConcreteStrategyA
from Strategy import ConcreteStrategyB
from Strategy import ConcreteStrategyC
from Strategy import Context


# 修改后的上下文
class ContextF(Context):
    # 参数不是具体的策略对象，而是字符串
    # 将实例化策略的过程由客户端转移到上下文类中（简单工厂的应用）
    def __init__(self, type : str):
        # 此处如果添加策略，需要修改代码
        # 抽象工厂模式中讲到反射技术可以有更好的方法
        if type == "A":
            self.strategy = ConcreteStrategyA()
        elif type == "B":
            self.strategy = ConcreteStrategyB()
        elif type == "C":
            self.strategy = ConcreteStrategyC()
        else:
            raise TypeError("unknown strategy type!")



# 客户端程序
def main():
    # 客户端只需要认识一个上下文类, 无需认识策略类
    context = ContextF("A")
    context.ContextInterface()
    context = ContextF("B")
    context.ContextInterface()
    context = ContextF("C")
    context.ContextInterface()


if __name__ == "__main__":
    main()
