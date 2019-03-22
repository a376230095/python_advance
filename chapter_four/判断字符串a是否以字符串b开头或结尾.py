'''
某系统目录有以下的文件
a=["quicksort.c","graph.py","heap.java","install.sh","stack.cpp"]
挑选出所有的.sh文件和.py文件
'''
#用str.startswith()和str.endswith()
import os
#listdir是取出文件夹中的所有文件，参数file是取file文件夹下的所有文件，保存成列表
a=os.listdir("file")
#如果字符串的结尾包含.py和.sh，，这里是or的关系，返回True，只接受元祖，可以是但元素
b=a[0].endswith((".py",".sh"))
#用列表解析解决问题
files=[x for x in a if x.endswith((".py",".sh"))]
print(files)
