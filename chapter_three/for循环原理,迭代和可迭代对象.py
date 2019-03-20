#a和c都是可迭代的对象，其中iter(c)可以生成一个迭代器
#实际使用了c.__iter__()的方法，两者等价
#c.next()方法会返回1，第二次用返回2，第三次用返回3，第四次用触发StopIteration

c=[1,2,3]
#c会先变成iter(c)，也就是c.__iter__()
#第一次使用i=c.next，直达触发StopIteration停止
for i in c:
    pass
#a会先变成iter(a)也就是a.__getitem__(),接下步骤和上面一样
a="abc"
for i in a:
    pass