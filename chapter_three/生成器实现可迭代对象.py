'''
实现一个可迭代的对象的类，能迭代出给定范围内的所有素数
pn = PrimeNumbers(1,30)
for k in pn:
    print(k)
输出结果：2 3 5 7 11 13 17 19 23 29
'''
#定义PrimeNumber类
class PrimeNumber():
    #构造方法包含start，stop，就是起始的值
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop

    #定义单个数字是否是素数
    def primeNumer(self,k):
        #0、1、2肯定不是素数，返回False
        if k<2:
            return False
        #遍历从2和小于k的数字
        for i in range(2,k):
            #当k与i没有余数，肯定不是素数
            if k%i==0:
                return False
        #当循环一遍，都有余数，肯定是素数
        else:
            return True

    #定义迭代对象，自动成为可迭代对象
    def __iter__(self):
        #k从其起始值取，stop+1是因为range的原因
        for k in range(self.start,self.stop+1):
            #self.primeNumer(k)返回Ture，就是素数
            if self.primeNumer(k):
#是素数才执行yield，等于保留了现场，并返回素数k，只有next才运行下去
                yield k

#由于PrimeNumber(1,100)就是有__iter__()方法，可以被迭代
#由于有yield，等于有next功能
for i in PrimeNumber(1,100):
    print(i)

'''
#求素数
a=[]
for i in range(3,100):
    flag=True
    for j in range(2,i):
        if i%j==0:
            flag=False
            break;
    if flag:
        a.append(i)
print(a)
'''