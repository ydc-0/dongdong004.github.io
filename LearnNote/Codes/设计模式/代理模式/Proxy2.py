# 静态代理与动态代理 https://www.jianshu.com/p/9cdcf4e5c27d
# python 动态代理机制 https://blog.csdn.net/water_likud/article/details/80566177
from types import MethodType


class HandlerException(Exception):
    def __init__(self, cls):
        super(HandlerException, self).__init__(cls, 'is not a hanlder class')


class InvocationHandler(object):
    def __init__(self, obj, func):
        self.obj = obj
        self.func = func

    def __call__(self, *args, **kwargs):
        print('handler:', self.func, args, kwargs)
        return self.func(*args, **kwargs)


class Proxy(object):
    def __init__(self, cls, hcls):
        self.cls = cls
        self.hcls = hcls
        self.handlers = dict()

    # 这儿的call在调用对象的方法时调用
    def __call__(self, *args, **kwargs):
        print("call method in proxy...")
        self.obj = self.cls(*args, **kwargs)
        return self

    def __getattr__(self, attr):
        print('get attr', attr)
        isExist = hasattr(self.obj, attr)
        res = None
        if isExist:
            res = getattr(self.obj, attr)
            print(type(res))
            if isinstance(res, MethodType):
                if self.handlers.get(res) is None:
                    self.handlers[res] = self.hcls(self.obj, res)
                return self.handlers[res]
            else:
                return res
        return res

    def add(self, x, y):
        print("overwrite add ...")
        return x + y


class ProxyFactory(object):
    def __init__(self, hcls):
        if issubclass(hcls, InvocationHandler) or hcls is InvocationHandler:
            self.hcls = hcls
        else:
            raise HandlerException(hcls)

    # 关于 call 方法 https://www.e-learn.cn/content/python/2679729
    # 这儿用作装饰器，在被装饰的类实例化时调用
    def __call__(self, cls):
        return Proxy(cls, self.hcls)


# 这儿使用装饰器实现 AOP
@ProxyFactory(InvocationHandler)
class Sample:
    def __init__(self, age):
        self.age = age

    # 这儿的方法可以被 Proxy 重写
    def foo(self):
        print('hello', self.age)

    def add(self, x, y):
        return x + y


def main():
    s = Sample(12)
    print(type(s))
    s.foo()
    s.add(1, 2)
    print(s.age)


if __name__ == "__main__":
    main()
