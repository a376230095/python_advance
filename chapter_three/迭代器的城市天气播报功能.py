'''
从网络抓取天气信息，依次显示执行
北京：15~20
天津：17~22
长春：30~40
...
如果一次抓取所有城市天气再显示，显示第一个城市气温时，有很高的延迟，并且会浪费存储空间，
期望以“用时访问”的策略，并且能把所用的城市天气封装到一个对象，用for语句进行迭代

方法：使用collections import Iterable,Iterator的类，继承他们，实现一个迭代对象
'''
import requests
from collections import Iterable,Iterator

#创建一个天气的迭代器，实现next的功能，继承Iterator迭代器
class WeatherItertor(Iterator):
    def __init__(self,cities):
        #初始化列表cities，索引index初始0
        self.cities=cities
        self.index=0
    #这个获取单个城市天气的逻辑代码
    def forecast(self,city):
        #请求的url
        url = "http://wthrcdn.etouch.cn/weather_mini?city=" + city
        r = requests.get(url)
        #进一步优化数据
        data = r.json()["data"]["forecast"][0]
        #返回的格式“北京:(low:低温 6℃,high高温 20℃)”
        return "{}:({},{})".format(city, data["low"], data["high"])

    #实现next方法
    def __next__(self):
        #当索引=城市的数量时，就迭代完毕，引发StopIteration
        if self.index==len(self.cities):
            raise StopIteration
        #获取单个城市，提取城市列表当前的索引值
        city=self.cities[self.index]
        #使用一次记得索引+1，不然一直无法跳出循环
        self.index+=1
        #返回当前城市的天气情况
        return self.forecast(city)

#创建一个可迭代对象天气
class WeatherIterable(Iterable):
    def __init__(self,cities):
        #为了可以使用WeatherIterable(["北京","上海"])加入的citites
        self.cities=cities

    #当变成迭代对象时，就返回迭代器
    def __iter__(self):
        return WeatherItertor(self.cities)

for i in WeatherIterable(["深圳","上海"]):
    print(i)