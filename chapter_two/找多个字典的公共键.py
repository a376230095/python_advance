#三场比赛，进球人员和
from random import randint,sample
#从sample的字符串中，随机找5个不重复的值
#只要里面是序列即可，比如列表、元祖、字符串
a=sample("abcdefg",5)
#字典解析创建每一场球员的随机进球数，x是球员名字，randint(1,3)是进球数
s1={x:randint(1,3) for x in sample("abcdefg",randint(3,7))}
s2={x:randint(1,3) for x in sample("abcdefg",randint(3,7))}
s3={x:randint(1,3) for x in sample("abcdefg",randint(3,7))}

'''
#方法一，遍历s1的值，当某一个值在s2并且在s3，表示这个值，都在里面，是公共键
for k in s1.keys():
    if k in s2.keys() and k in s3.keys():
        print(k)


#方法二，集合并集的方式
#set的方式把字典变成集合，默认取set
s1,s2,s3=set(s1),set(s2),set(s3)
# &的方式是交集，|是并集
print(s1 & s2 & s3)
'''
#通过map和reduce的方式
from functools import reduce
#map接受两个参数，一个是函数名，一个是可迭代的对象
#输出[{'e', 'a', 'b'}, {'d', 'c', 'f', 'g', 'b'}, {'c', 'g', 'a', 'f'}]
print(list(map(set,[s1,s2,s3])))
#reduce接受两个参数，一个是函数名，一个是可迭代的对象
#引用a和b，返回a和b的并集，在map那里去拿，拿完两个之后的并集，拿第三个s3，再并集
print(list(reduce(lambda a,b:a&b,map(set,[s1,s2,s3]))))
