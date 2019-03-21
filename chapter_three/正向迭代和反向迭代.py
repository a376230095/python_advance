"""
实现类似range的循环，(3.0,4.0,0.2)
正向迭代：3.0-3.2-3.4-3.6-3.8-4.0
反向迭代：4.0-3.8-3.6-3.4-3.2-3.0
"""

'''
#反向迭代的例子
a=[1,2,3,4,5]

#这样会改变a，不推荐
#a.reverse()

#虽然不会改变a，这样会创建一个列表，浪费空间
#b=a[::-1]

#这种方法不会改变原来的a，也不会创建东西
#reversed(a)其实是用了a的a.__reversed__的方法，我们重写这个方法
for i in reversed(a):
    print(i) #5 4 3 2 1
'''

class FloatRange():
    #定义三个初始值，开始、结束、步进
    def __init__(self,start,stop,step):
        self.start=start
        self.stop=stop
        self.step=step

    #重写__iter__方法
    def __iter__(self):
    #初始值就是一开始的start
        first=self.start
    #当first小于stop，就会一直循环下去
        while first<=self.stop:
    #保存第一个first值，return first，等下一个next()才执行
            yield first
    #实现步进的功能
            first+=self.step

    #重写__reversed__反向的方法
    def __reversed__(self):
    #第一个last值就是最后的值
        last=self.stop
    #当last永远小于大于初始值，就一直循环
        while last>=self.start:
    #保存了第一个值，然后返回第一个last，下一次next()才继续
            yield last
    #实现步进的功能
            last-=self.step

#这个是反向迭代
for i in reversed(FloatRange(1.0,4.0,0.5)):
    print(i)

#这是正向的迭代
for i in FloatRange(1.0,4.0,0.5):
    print(i)


