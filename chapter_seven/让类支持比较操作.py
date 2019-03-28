'''
自定义的类的实例可以使用比较运算符
比如定义一个矩形的类，可以比较他们的面积
'''


# 如果每个大于、小于、大于等于都实现，会非常的麻烦
# 使用total_ordering这个装饰器可以简化，只需要重写小于、等于两个方法即可
from functools import total_ordering

#如果我们定义了一个圆的class，那么圆要和三角形比较，肯定又要实现__lt__等方法很麻烦
#因此定义一个抽象的父类，把共有的__lt__等方法集合在一起，只实现area的抽象方法，因为面基计算方式不一样
#引用抽象的模块
from abc import ABCMeta,abstractmethod
from math import pi
#三角形和圆形的情况
@total_ordering
#定义Shape的父类
class Shape():
    #这个是抽象方法的引用，所以继承的子类都要实现这个方法
    @abstractmethod
    def area(self):
        pass

    #先重写__lt__方法
    def __lt__(self,obj):
        return self.area() < obj.area()

    #再重写__eq__方法
    def __eq__(self, obj):
        return self.area() == obj.area()

class Rectangle(Shape):
    def __init__(self,w,h):
        self.w=w
        self.h=h

    def area(self):
        return self.w*self.h

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return self.radius**2 * pi

c1=Circle(5)
r1=Rectangle(1,1)
print(c1>r1)
'''
#这个是指一种三角形的情况
@total_ordering
class Rectangle:
    def __init__(self,w,h):
        self.w=w
        self.h=h

    def area(self):
        return self.w*self.h

    #先重写__lt__方法
    def __lt__(self,obj):
        return self.area() < obj.area()

    #再重写__eq__方法
    def __eq__(self, obj):
        return self.area() == obj.area()

rect1=Rectangle(5,3)
rect2=Rectangle(4,4)
rect3=Rectangle(4,4)
#实际调用rect1.__lt__(rect2)
print(rect1<rect2) #rect1.area()>rect2.area()
print(rect1!=rect2)
print(rect3==rect2)
'''