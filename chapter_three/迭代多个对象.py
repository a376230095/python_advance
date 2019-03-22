'''
1、一个班考试成绩，语文、数学、数学分别存储3个列表中，同事迭代3个列表，计算每个学生的总分
2、一个年级有3个班，每班英语成绩分别存储4个列表中，一次迭代每个列表，统计全年成绩最高的90分人数
'''
from random import randint

#第一题
'''
#新建三个成绩表
chinese=[randint(60,100) for x in range(10)]
math=[randint(60,100) for x in range(10)]
english=[randint(60,100) for x in range(10)]
score=[]
#遍历列表的总数
for i in range(len(chinese)):
#把三个成绩相加起来
    score.append(chinese[i]+math[i]+english[i])
print(score)
'''

'''
chinese=[randint(60,100) for x in range(10)]
math=[randint(60,100) for x in range(10)]
english=[randint(60,100) for x in range(10)]
total=[]
#利用zip组成一个多元祖的列表，进行相加总成绩
for c,m,e in zip(chinese,math,english):
    total.append(c+m+e)
print(total)
'''
#第二题

from itertools import chain
#chain的作用是把多个可迭代对象变成串行类型
#比如a=[1,2],b=[3,4],charin(a,b)就变成[1,2,3,4]
c1=[randint(60,100) for x in range(10)]
c2=[randint(60,100) for x in range(10)]
c3=[randint(60,100) for x in range(10)]
c4=[randint(60,100) for x in range(10)]
count=0
#将四个班的成绩合在一起，形成一个列表，然后再统计出大于90分的人
for i in chain(c1,c2,c3,c4):
    if i>=90:
        count+=1
print(count)






