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

    #设置R属性，用property方法，第一个接受get方法，第二个接收set方法
    R=property(getRadius,setRadius)
    #设置A属性，获得get面积的方法
    A=property(getArea)

c=Circle(5)
'''
#如果可以随意更改属性，会很危险
c.radius='abc'
#计算面积会报错，因为半径不能是abc
print(c.getArea())
#使用方法又繁琐，如果可以用类似属性的调用，会方便很多
c.setRadius(6)
c.getRadius()
'''
#c.R等于使用getRadius()方法
print(c.R)
#c.R=5等于使用setRadius(6)
c.R=5
#c.A等于使用getArea()方法
print(c.A)
