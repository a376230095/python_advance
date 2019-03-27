'''
某网络游戏，定义玩家类player(id,name,status,...)
每有一个在线玩家，服务器就有一个player的实例
如何降低大量实例的内存开销
'''
class Player(object):
    def __init__(self,uid,name,status=0,level=1):
        self.uid=uid
        self.name=name
        self.stat=status
        self.level=level

class Player2(object):
    #定义这个可以去掉__dict__属性，减少内存消耗
    __slots__=['uid','name','stat','level']
    def __init__(self,uid,name,status=0,level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level

p1=Player('001','tong')
p2=Player2('001','tong')

#查看p1的全部属性和p2的全部属性，变成set类型
p3=set(dir(p1))
p4=set(dir(p2))
#set类型就可以相加减了，就知道p1比p2多了什么属性
print(p3-p4) #{'__dict__', '__weakref__'}

#__dict__会先默认帮我们存储uid,name,status=0,level=1，我们还可以添加一些属性
#比如添加a，这个值是b，那么就非常浪费内存了
p1.__dict__["a"]="b"
print(p1.a)

#因此如果使用__slots__=['uid','name','stat','level']，就限定了我们的属性值，就不会有那么多属性了
