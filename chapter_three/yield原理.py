'''
#https://blog.csdn.net/mieleizhi0522/article/details/82142856
#yield相当于return,yield 4相当于return 4,当遇到了yield，函数就停止运行了，保存为一个生成器
#等下次用next方法调用时，才会继续运行

def f():
    print("in f()1,1")
    yield 1
    print("in f()1,2")
    yield 2
    print("in f()1,3")
    yield 3

#保存运行的f()函数为一个变量g
g=f()
#如果不使用next方法，这个f()虽然是执行的状态，但不会执行，因为有yield,第一个print也不会执行
#第一个next方法执行了，先执行print("in f()1,1")，然后执行yield 1，等于return 1，程序结束，保存函数执行的现场
print(g.__next__())
#第二个next方法执行，因为保存了现场，所以从yield 1下面执行，执行print("in f()1,2")，执行yield 2，返回2，程序结束
print(g.__next__())
#第二个next方法执行，因为保存了现场，所以从yield 2下面执行，执行print("in f()1,3")，执行yield 3，返回3，程序结束
print(g.__next__())
#这时候已经没有yeild，就爆出stopiteration错误，和迭代器是一样的
print(g.__next__())
'''

def foo():
    print("starting...")
    while True:
        res=yield 4
        print("res:",res)

a=foo()
#第一个next方法，运行print("starting...")，然后运行while，res=yield 4,会先运行yield 4
#程序就结束了，return了4，后面的赋值不执行了
print(a.__next__())
#运行输出********************
print("*"*20)
#第二个next方法，程序执行res=，由于yield 4一早就return 4出去了，res只能等于None了
#然后执行("res:",res)，所以就是res: None，继续执行while Ture，回到res=yield 4
#先执行yield 4，return了4，程序结束
print(a.__next__())
#程序到了res=，由于send了一个6，等于res=6，然后print("res:",res)，就是res: 6
#继续执行whilt True，回到res=yield 4，先执行yield 4，return了4，程序结束
print(a.send(6))
