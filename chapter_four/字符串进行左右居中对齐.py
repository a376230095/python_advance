'''
某个字段存储一系列属性
{
    “Loddist”:100,
    “smallCull”:0.04,
    “discull”:500.0,
    “trilinear”:40
}
在程序中，我们想以一下工整的格式将其输出
Loddist=  :100,
smallCull :0.04,
discull   :500.0,
trilinear :40
'''

#对齐的办法，我们可以用左右对齐，str.ljust和rjust
a={
    "Loddist":100,
    "smallCull":0.04,
    "discull":500.0,
    "trilinear":40
}
#计算出key的字符串个数，然后求出最大值，用最大值来左对齐
b=max(map(lambda x:len(x),a.keys()))
#循环整个字典
for k,v in a.items():
    #用ljust进行左对齐
    print(k.ljust(b)+":"+str(v))