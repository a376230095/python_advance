'''
读取文件100~300行的内容，是否可以使用切片的方式得到100~300行的内容的生成器
f=open('/Var/log/dmesg')
'''

'''
with open ("test") as a:
#通过转化成readlines，就可以切片，但是会创建c，等于重新跑一次，浪费资源
    c=a.readlines()
    print(c[100:300])
'''
#运用islice
from itertools import islice
with open ("test") as a:
#islice接受三个参数，第一个可迭代对象，第二个是初始值，第三个是结束值，第四个是step
#这样就获取到了100到300行了一个迭代器了
    c=islice(a,100,300)
#如果是前100行，就是is(a,100)
#如果是从100行到最后一行，就is(a,100,None)
#这个a和文件一样，会消耗的，等于是读完就没有的了类型

'''
这个例子可以不看
class A():
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop

    def yewu(self):
        with open("test") as a:
            return a.readlines()

    def __iter__(self):
        first=self.start
        while first<=self.stop:
            yield self.yewu()[first-1]
            first+=1

for i in A(100,300):
    print(i,end="")
'''