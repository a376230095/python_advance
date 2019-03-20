#用字典存储每个人答题的速度，先回答的人先记录
#存储后字典没有序列，按先后顺序存储也无法体现谁先谁后

'''
#引用collections
from collections import OrderedDict
#创建一个有序列的字典
d=OrderedDict()
#先加入的肯定是序列1，然后2、3
d["one"]=(2,17)
d["two"]=(3,18)
d["three"]=(4.14)
for a in d.keys():
    # 结果one two three，是按顺序输出
    print(a,end=' ')
'''
#利用time、random实现学生交卷时间、排名的案例
from collections import OrderedDict
from time import time
from random import randint
#创建7个学生，分别是a、b、c等，用列表保存
allStudent=list("abcdefg")
#新建一个字典保存结果
d=OrderedDict()
#设置考试开始的时间，就是当前程序运行的起始时间
start=time()
#有多少学生就循环多少次，7个学生循环七次
for i in range(7):
    #用input模拟，当回车时，就是该学生交卷的时间了
    input()
    #交卷结束时间就是input按回车后的时间
    end=time()
    #随机获取当前交卷的学生，用pop保存一个学生，既可以完美减少一个学生，又可以保存这个学生
    #6-i是第一次i为0，从0~6元素范围取一个，当i=1，则是从0~5取一个
    student=allStudent.pop(randint(0,6-i))
    #key为学生的名字，value的i+1是名次，第一次i为0，名次从第一名开始，需要+1
    #end-start就是答题的时间是多少
    d[student]=(i+1,end-start)
    #每次input回车后，输出当前的学生名字，名次和答题时间
    print(student,i+1,end-start)

print(d)




