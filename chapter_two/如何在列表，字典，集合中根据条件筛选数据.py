'''
过滤列表[3,9,0,-2,-4]中的负数
筛选字典{"tong":80,"zeng":95}高于90分的人
筛选集合{77,89,32,20}中能被3整除的元素
'''

'''
#通常的方法，迭代循环
a=[3,9,0,-2,-4]
b=[]
for i in a:
    if i>=0:
        b.append(i)
'''
from random import randint
'''

from timeit import timeit

#列表生成式随机生成10个-10到10的数字
a = [randint(-10,10) for i in range(1,10)]
#filter接受两个参数，一个是函数，一个是可迭代的对象，把不满足的值舍弃
#lambda直接return x>=0,就不用加if了，加了if反而会报错
data=list(filter(lambda x:x>=0,a))
print(data)

#列表生成式的方式
data=[x for x in a if x>=0]
print(data)
'''

a={x:randint(60,100) for x in range(1,21)}
print(a)
[x for x in a if x.ke>90]