'''
1、过滤掉用户输入中多余的空白字符串：
"   nick2008@gamil.com   "
2、过滤掉windows下编辑文本中的"\r"
'hello world\r\n'
3、去掉文本中的unicode自核音符（音调）
额，不会打这个音符
'''
#第一题，使用strip方法，有lstrip和rstrip去掉空格
a="   nick2008@gamil.com   "
#默认把两端的空格都去掉
print(a.strip())

#第二题，用replace或者正则re.rub的方法
a='hello world\r\n'
#把"\r"给去掉，等于是替换嘛
b=a.replace("\r","")
print(b)

#第三题
