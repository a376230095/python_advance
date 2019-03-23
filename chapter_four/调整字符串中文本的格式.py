'''
某软件的log文件，日期格式为"yyyy-mm-dd:"
2016-03-04 hello f
2016-03-04 hello f
2016-03-04 hello f
2016-03-04 hello f

吧日期改为美国日期'mm/dd/yyyy'，2016-03-04变成03/04/2016
'''
import re
with open("time.log") as log:
    log=log.read()
#sub方法接受3个参数，第一个是匹配的值，第二个是替换匹配的值，第三个是对那个字符串进行匹配
#通过分组的方法，(\d{4})-(\d{2})-(\d{2})，第一组是(\d{4})，第二组是(\d{2})
#使用是第一组\1，第二组\2，必须用r来弄
    logA=re.sub("(\d{4})-(\d{2})-(\d{2})",r"\2/\3/\1",log)
    print(logA)