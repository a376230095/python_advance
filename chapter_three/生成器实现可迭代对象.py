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

class PrimeNumber():
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop

    def primeNumer(self,k):
        if k==1 or k==2 or k==0:
            return False
        for i in range(2,k):
            if k%i==0:
                return False
        else:
            return True

    def __iter__(self):
        for k in range(self.start,self.stop+1):
            if self.primeNumer(k):
                yield k

for i in PrimeNumber(3,100):
    print(i)