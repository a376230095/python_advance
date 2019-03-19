#英语成绩{"tong":"88"，"zeng":"85"，"chen":"50"}进行排序

#第一种方法，zip转化成元祖进行排序
#元祖是可以排序的，比如(90,'a')>(60,'b')
from random import randint
a={x:randint(60,100) for x in range(10)}
#利用zip，组成一个字典的值和键的一对元祖
b=list(zip(a.values(),a.keys()))
#再对元祖排序
print(sorted(b))
#第二种方法，直接用对字典的items排序，用key和匿名函数
print(sorted(a.items(),key=lambda item:item[1]))