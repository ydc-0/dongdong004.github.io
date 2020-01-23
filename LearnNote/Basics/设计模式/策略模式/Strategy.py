# -*- coding: utf-8 -*-


# 抽象算法类
class Strategy(object):
    # 抽象算法
    def AlgorithmInterface(self):
        pass


# 具体算法A
class ConcreteStrategyA(Strategy):
    def AlgorithmInterface(self):
        print("A 实现")


# 具体算法B
class ConcreteStrategyB(Strategy):
    def AlgorithmInterface(self):
        print("B 实现")


# 具体算法C
class ConcreteStrategyC(Strategy):
    def AlgorithmInterface(self):
        print("C 实现")


# 上下文
class Context(object):
    # 初始化时，传入策略对象
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    # 根据策略对象，调用具体的方法
    def ContextInterface(self):
        self.strategy.AlgorithmInterface()


# 客户端程序
def main():
    # 实例化不同的策略
    context = Context(ConcreteStrategyA())
    context.ContextInterface()
    context = Context(ConcreteStrategyB())
    context.ContextInterface()
    context = Context(ConcreteStrategyC())
    context.ContextInterface()


if __name__ == "__main__":
    main()
