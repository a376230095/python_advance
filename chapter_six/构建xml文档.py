'''
将csv转化成xml
Data,Open,High,Low,Close,Volume,Adj close
2016-06-30,8.69,8.74,8.66,8.70,36220400,8.70
转化成以下的格式xml格式
<Data>
    <Row>
        <Date>2016-06-30</Date>
        <Open>8.69</Open>
        <High>8.74</High>
        <Low>8.66</Low>
        <Close>8.70</Close>
        <Volume>36220400</Volume>
        <AdjClose>8.70</AdjClose>
    </Row>
</Data>
'''
#导入Element,ElementTree
from xml.etree.cElementTree import Element,ElementTree,tostring
'''

#创建一个xml元素Data
e=Element("Data")
#设置元素Data的属性的key和value
e.set("name","tong")
#设置元素Data的text数值
e.text="10"
#通过tostring方法打印出当前的xml格式
print(tostring(e))  #b'<Data name="tong">10</Data>'
#添加一个子元素Row
e1=Element("Row")
#设置子元素的text
e1.text="11"
#append方法添加子元素
e.append(e1)
print(tostring(e))
#ElementTree(e)将e弄成一个tree
f=ElementTree(e)
#弄成tree才可以把这个写入文件中
f.write("create.xml")
'''
import csv
with open("finance.csv") as c:
    #读取金融的的csv元素
    c=csv.reader(c)
    #读取头部信息Data,Open,High,Low,Close,Volume,Adj close
    header=c.__next__()
    #创建root的元素
    root = Element("Date")
    #遍历这个金融csv，读取每一行
    for row in c:
        #每一行就创建root的子元素Row
        Row=Element("Row")
        #马上将这个子元素Row弄到root中
        root.append(Row)
        #zip可以组成1个两元祖的列表，header就是tag，row就是数据了
        for tag,text in zip(header,row):
            #创建孙元素e，tag是header的内容
            e=Element(tag)
            #text就是row的数据内容
            e.text=text
            #将这个e加载到Row中
            Row.append(e)
    #创建一个tree对象
    f=ElementTree(root)
    #写入到文件当中
    f.write("create.xml")
















