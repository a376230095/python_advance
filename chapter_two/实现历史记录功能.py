#创建一个猜谜的小游戏，记录用户猜的历史记录

from random import  randint
a=randint(0,100)
def guess():
    c=int(input("please input guess number"))
    if c==a:
        print("guess secessful")
    elif c>a:
        print("guess number is bigger than correct numbr")
    else:
        print(print("guess number is small than correct numbr"))
    return c

while True:
    c=guess()
    if c==a:
        break
