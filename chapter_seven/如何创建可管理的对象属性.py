'''
在面向对象编程中，我们把方法看作是对象的接口
直接访问对象的属性是不安全的，或设计上不够宁或
但是使用调用方法在形式上不如访问属性简洁
circle.getRadius()
circle.setRadius(5.0) #繁

circle.radius
circle.radius=5.0 #简
能否在形式上是属性访问，但实际上调用方法
'''
from math import  pi
class Circle():
    def __init__(self,radius):
        self.radius=radius

    def getRadius(self):
        return self.radius

    def setRadius(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError("wrong type.")
        self.radius=value

    def getArea(self):
        return self.radius** 2* pi

c=Circle(5)
print(c.getArea())