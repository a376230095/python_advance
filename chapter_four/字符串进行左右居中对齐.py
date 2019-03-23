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
