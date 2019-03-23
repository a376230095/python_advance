'''
一个UDP的参数如下：
hwDetect:    "<0112>"
gxDepthBits: "<32>"
gxResolution:"<1024*768>"
gxRefresh：  "<60>"
fullAlpha    "<1>"
lodDist：    "<100.0>"
DisCull      "<500.0>"

我们收集<>这里的数据，弄成一个列表
["<0112>",<32>".......]
最终拼接一个字符串
"<0112><32>"
'''
import re
from functools import reduce
with open("UDP.txt",encoding="utf-8") as udp:
    udp=udp.read()
    #用正则表达找到<>的值
    udplist=re.findall("<.*?>",udp)

    #方法一，用字符串拼接的方法+，但是会生成很多个字符串，然后要消除，浪费空间
    udpstring=str(reduce(lambda x,y:x+y,udplist))

    #方法二，使用join,将列表转化成字符串，什么都不加刚刚好完成要求
    udpstring="".join(udplist)

    #加了";"，在每个列表拼接都有;
    a=";".join(udplist) #<0112>;<32>;<1024*768>;<60>;<1>;<100.0>;<500.0>

    #遇到有数字的问题，因为字符串和数字不能相加减，用列表生成式可以解决
    a=["c",1,2]
    #但是这样会浪费很多空间
    a = "".join([str(x) for x in a])
    #用生成器就可以解决问题了
    a = "".join((str(x) for x in a))
    print(a)