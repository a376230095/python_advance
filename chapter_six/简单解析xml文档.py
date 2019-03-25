"""
<xml version="1.0">
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
"""
#导入parse模块
from xml.etree.ElementTree import parse
with open("readXml.xml") as f:
    #parse接收一个文件的对象
    x=parse(f)

    #获取根目录
    root=x.getroot()

    #找到根下所有的"country"子元素，用列表保存
    countrys=root.findall("country")

    #找到根下的第一个"country"元素
    country_one=root.find("country")

    #获取country属性的名称
    print(country_one.get("name"))

    #iterfind和findall一样，只是这个是创造一个生成器对象
    root.iterfind('country')

    #会生成一个生成器对象，遍历整个root的子和孙等孙孙对象
    root.iter()

    #iter可以找到任意子、孙的rank这个标签的对象,找到三个，就是三个rank
    ranks=root.iter("rank")

    #转化成list
    ranks=list(ranks)

    #text获取text文本
    print(ranks[0].text)

    #高级的xpath功能

    #*表示获取该节点下的全部元素
    a=root.findall("country/*")

    #..表示父节点，取rank下的父节点
    b = root.findall('.//rank/..')

    #/表示从根节点取

    #.表示当前节点， //表示从当前节点取，从root节点获取全部的rank对象
    d=root.findall('.//rank')

    #[@name=xxx]表示取country下name这个属性
    c=root.findall('country[@name]')


    # [@name=xxx]表示取country下name这个属性等于Liechtenstein的对象
    d = root.findall('country[@name="Liechtenstein"]')

    # [name]表示取country这个对象，包含有rank这个子对象
    e = root.findall('country[rank]')

    # [name]表示取country这个对象，包含有rank="2"这个子对象
    f= root.findall('country[rank="2"]')
    print(f)
























