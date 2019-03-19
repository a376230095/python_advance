#统计序列中元素出现的频度

#对某英文文章的单词，进行词频统计，找到出现次数最高的10个单词，出现的次数是多少

from random import randint
'''
#第一种low的方法
#某个随机序列[12,5,4,5,6,6,7，6]中找到出现最高的3个元素，他们的出现次数是多少

#生成20个随机的1~10的数字
a=[randint(1,10) for i in range(20)]
#创建一个字典，key是列表a的值，0是value的初始值，因为key唯一，可以保证key唯一
b=dict.fromkeys(a,0)
#遍历a，当出现一次数字，就字典的value就+1
for i in a:
    b[i]+=1
#排序，从大到小，根据value的值，排序的结果是列表中的元祖
print(sorted(b.items(),key=lambda item:item[1],reverse=True))
'''
'''

#Counter字面意思就是统计数量了
from collections import Counter
#生成20个随机的1~10的数字
a=[randint(1,10) for i in range(20)]
#创建一个字典d，a里面的值就是key且唯一，还统计了每个key出现的次数（value）
d=Counter(a)
#返回前三个出现次数最多的值，用列表内嵌元祖表现
print(d.most_common(3))
'''
import re
from collections import Counter
with open("tong.txt") as file:
    txt=file.read()
    #result=re.split(".\W",txt)
    #findall去的正则找到全部的单词，用\w+的贪婪模式，保存为列表
    result=re.findall("\w+",txt)
    a=Counter(result)
    print(a.most_common(9))






