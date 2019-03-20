#创建一个猜谜的小游戏，记录用户猜的历史记录
from collections import deque
from random import randint

d=[]
history=deque(d,5)
a=randint(0,100)
print(a)
def guess():
    c=int(input("please input guess number"))
    if c==a:
        print("guess secessful")
    if c>a:
        print("guess number is bigger than correct numbr")
    if c<a:
        print("guess number is bigger than correct numbr")
    return c


while True:
    c=guess()
    if c==a:
        history.append(c)
        break
        history.append(c)
#如何保存这个history的值，用pickle
print(history)
import pickle
#存储history到文件history
pickle.dump(history,open("history","wb"))
history2=pickle.load(open("history","rb"))
print(history2)


