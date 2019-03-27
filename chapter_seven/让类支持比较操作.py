'''
自定义的类的实例可以使用比较运算符
比如定义一个矩形的类，可以比较他们的面积
'''
class Rectangle:
    def __init__(self,w,h):
        self.w=w
        self.h=h

    def area(self):
        return self.w*self.h

rect1=Rectangle(5,3)
rect2=Rectangle(4,4)
rect1>rect2 #rect1.area()>rect2.area()