#用元祖储存一类数据，比如学生的信息（年龄、性别、电话等）
#用元祖可以减少存储开销,但是用index，可读性太差，0代表性别不知道干嘛
#("jim",16,"male","jim8721@qq.com")
#("tong",18,"female","tong8721@qq.com")

student=("jim",16,"male","jim8721@qq.com")

'''
第一种方案
#用别名代替0,1,2,相当于枚举类型，但是枚举
#第一种写法
name=0
age=1
sex=2
#第二种写法
name,age,sex=0,1,2
#第三种写法
name,age,sex=range(3)


#打印姓名
#print(student[0])
print(student[name])

#if student[1]>0:
if student[age]>0:
    pass

#if student[2]=="male":
if student[sex]=="male":
    pass
'''
#第二种方案，用collection



#引用带有名称的元祖
from collections import namedtuple
#创建一个类student,括号第一个student是类名，后面的是元祖的index名称化的名称
student=namedtuple("student","name age sexe email")
#创建tuple实例，一一对应，比如name=tong
tong=student("tong",18,"male","3762300095@qq.com")
#打印tong就是一个元祖了
print(tong)
#可以通过.的方式直接引用name，就不用数字索引了
print(tong.name)
print(tong.email)

