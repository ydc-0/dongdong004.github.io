# -*- coding: utf-8 -*-
# 简单工厂模式的实现


# 抽象产品：汽车
class Car(object):
    # 抽象方法：由子类实现
    def drive(self):
        pass

    # 通用方法：子类可重写
    def description(self):
        print("This is a car.")


# 产品类：奥迪
class Audi(Car):
    def drive(self):
        print("drive Audi")


# 产品类：宝马
class Bmw(Car):
    def drive(self):
        print("drive Bmw")


# 产品类：奔驰
class Benz(Car):
    def drive(self):
        print("drive Benz")


# 工厂类：生产汽车
class Driver(object):
    def GetCar(self, type):
        if type == "Audi":
            return Audi()
        elif type == "Bwn":
            return Bwn()
        elif type == "Benz":
            return Benz()
        else:
            raise Exception("Driver:: no such type")


def main():
    driver_factory = Driver()
    my_car = driver_factory.GetCar("Benz")
    my_car.description()
    # 无需根据产品类型而改变调用方法
    my_car.drive()


if __name__ == "__main__":
    main()
