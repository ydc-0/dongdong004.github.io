# python 的装饰器
# https://www.jianshu.com/p/0655688fe5ad
# https://baijiahao.baidu.com/s?id=1599960767890712913&wfr=spider&for=pc


# 在Python中，AOP通过装饰器模式实现更为简洁和方便。
# 先来解释一下什么是AOP。AOP即Aspect Oriented Programming，中文翻译为面向切面的编程，
# 它的含义可以解释为：如果几个或更多个逻辑过程中（这类逻辑过程可能位于不同的对象，不同的接口当中），
# 有重复的操作行为，就可以将这些行为提取出来（即形成切面），进行统一管理和维护。
# 举例子说，系统中需要在各个地方打印日志，就可以将打印日志这一操作提取出来，作为切面进行统一维护。
# 从编程思想的关系来看，可以认为AOP和OOP（面向对象的编程）是并列关系，二者是可以替换的，也可以结合起来用。
# 实际上，在Python语言中，是天然支持装饰器的，如下例：


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

class LogManager(object):
    @staticmethod
    def log(func):
        def wrapper(*args, **kw):
            print('call %s():' % func.__name__)
            return func(*args, **kw)
        return wrapper

@log
def now():
    print("2020/03/11")

class MyClass(object):
    @LogManager.log
    def show(self):
        print("my class")

# 调用测试
def main():
    now()
    my = MyClass()
    my.show()


if __name__ == "__main__":
    main()
