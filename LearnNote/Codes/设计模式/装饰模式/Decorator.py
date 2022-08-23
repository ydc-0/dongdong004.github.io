

# 首先创建一个 人 类
class Person(object):
    def desc(self):
        print("This is a person.")


# Tom 先生
class Tom(Person):
    # 重写
    def desc(self):
        print("This is Tom.")


# 创建装饰器
class PersonDecorator(Person):
    # 持有被装饰类，以公共接口接收
    def __init__(self, person: Person):
        self.person = person

    # 重写
    def desc(self):
        self.person.desc()


# 创建修饰子类
class HighPerson(PersonDecorator):
    # 重写
    def desc(self):
        super().desc()
        print("He is very high!")


# 另一个修饰子类
class BeautifulPerson(PersonDecorator):
    # 重写
    def desc(self):
        super().desc()
        print("He is very beautiful!")


# 调用测试
def main():
    person = Tom()
    person.desc()
    print("------ high person ------")
    person = HighPerson(Tom())
    person.desc()
    print("------ beautiful person ------")
    person = BeautifulPerson(Tom())
    person.desc()


if __name__ == "__main__":
    main()
