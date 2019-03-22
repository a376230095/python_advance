'''
把某个字符串依据分隔符号拆分不同的字段
例如：s='ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
'''


s='ab;cd|efg|hi,jkl|mn\topq;rst,uvw\txyz'
#通过split先过滤掉";"
a=s.split(";") #a=['ab', 'cd', 'efg', 'hi,jkl', 'mn\topq', 'rst,uvw\txyz']
#创建一个空的列表，extend多个列表，append是增加一个元素，extend是在后面增加一个元素
t=[]
#忽略print和list，只看map，取a的每一个元素，然后对这个元素split，完了后就加入到元素当中
print(list(map(lambda x:t.extend(x.split("|")),a)))
#将结果放到a中['ab', 'cd', 'efg', 'hi', 'jkl', 'mn\topq', 'rst', 'uvw\txyz']
a=t
#就是重复动作了
t=[]
print(list(map(lambda a:t.extend(a.split(",")),a)))
print(t)
a=t
t=[]
print(list(map(lambda a:t.extend(a.split("\t")),a)))
print(t)

#可以通过函数+循环的方法实现上面的方法
s='ab;cd|efg|hi,,jkl|mn\topq;rst,uvw\txyz'
def splitone(s,a):
    #一定要把字符串先变成一个元素的列表，不知道为什么
    res=[s]
    for i in a:
        t=[]
        print(list(map(lambda x:t.extend(x.split(i)),res)))
        res=t
        #这个是判断有两个,,的情况，因为有空值，把空值去掉即可
    return [x for x in res if x]

print(splitone(s,",;|\t"))

import re
s='ab;cd|efg|hi,,jkl|mn\topq;rst,uvw\txyz'
#这个方法是把符合的正则表达给分隔掉，有一个+是1个或者多个
t=re.split(r'[,;|\t]+',s)
print(t)

