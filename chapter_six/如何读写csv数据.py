'''
以下是股市的csv表格
Data,Open,High,Low,Close,Volume,Adj close
2016-06-30,8.69,8.74,8.66,8.70,36220400,8.70
2016-06-29,8.69,8.74,8.66,8.70,56220300,8.70
2016-06-28,8.69,8.74,8.66,8.70,36220400,8.70
2016-06-27,8.69,8.74,8.66,8.70,56220600,8.70
2016-06-26,8.69,8.74,8.66,8.70,36220800,8.70
2016-06-25,8.69,8.74,8.66,8.70,46220900,8.70
2016-06-24,8.69,8.74,8.66,8.70,36220300,8.70
2016-06-23,8.69,8.74,8.66,8.70,56220600,8.70
2016-06-22,8.69,8.74,8.66,8.70,36220200,8.70
提取出超过50000000点的数值到另一个csv文件中
'''
#导入csv模块
import csv
#csv本身就是文本文件Comma-Separated Values，所以不用加b
with open("finance.csv") as finance:
    #读取csv文件，read是一个可迭代的对象，只能用next或者for，每次输出一行
    read=csv.reader(finance)
    #读取要写的文件
    with open("finance_result.csv","w") as finance_result:
        #创建一个可写的对象
        write=csv.writer(finance_result)
        #先保存第一行读取的内容
        header=read.__next__()
        #把第一行的内容写入到新文件上
        write.writerow(header)
        #遍历整个csv
        for row in read:
            #当每行的第五个数值大于50000000就写入，记得要转化成int类型
            if int(row[5])>50000000:
                write.writerow(row)



#_csv.Error: iterator should return strings, not bytes (did you open the file in text mode?)
#出现这个问题，应该是读取的文件不是二进制的