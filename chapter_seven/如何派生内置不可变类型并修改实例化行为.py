'''
定义一种新类型的元祖，传入可迭代对象，我们只保留int类型的值且大于0的元素
例如intTuple([1,-1,abc,6,['x','y'],3])=>(1.6.3)
要求intTuple是内置tuple的子类
'''
class intTuple(tuple):
    def __new__(cls,iterable):
        g=(x for x in iterable if isinstance(x,int) and x>0)
        return super(intTuple,cls).__new__(cls,g)

    def __init__(self,iterable):
        super(intTuple,self).__init__()

a=intTuple([1,-1,'abc',6,['x','y'],3])
print(a)