

# 抽象主题角色：
class Subject(object):
    def method(self):
        print("subject method")


# 具体主题角色：
class RealSubject1(Subject):
    # overwrite
    def method(self):
        print("real method 1")


# 代理角色（静态代理）：
class Proxy(Subject):
    def __init__(self, subject: Subject):
        self.subject = subject

    def method(self):
        print("proxy ....")
        self.subject.method()


def main():
    # 静态代理, 创建 subject 的部分可以应用工厂模式对客户端隐藏
    subject = RealSubject1()
    proxy = Proxy(subject)
    proxy.method()


if __name__ == "__main__":
    main()
