import monkey
'''
姓名	语文	数学	外语
李雷	95	99	96
韩梅	98	100	93
张峰	94	95	95
计算出总分，并输出到另一个文件上
'''
import xlrd,xlwt

'''
#读取整个excel文件
book=xlrd.open_workbook("test.xlsx")
#读取一个sheet1，用index的方式读取第一张
sheet1=book.sheet_by_index(0)
获取cell单元格，传入行号和列号，这里的值会包含类型和数值的列表
cell1=sheet1.cell(1,1)
print(cell1.value)
# ctype类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
print(cell1.ctype)
#row为第二行的所有数据，包括类型和数值
print(sheet1.row(1))
#row为第二列的所有数据，包括类型和数值
print(sheet1.col(1))
'''

book=xlrd.open_workbook("test.xlsx")
sheet=book.sheet_by_index(0)
#nc获取有多少行
nc=sheet.ncols

#put_cell包含#行、列、类型、数值、风格的参数，没有风格就是None
#添加第1行，第5列，类型是字符串，value是总分
sheet.put_cell(0,nc,1,"总分",None)
#只统计总分，只在一列中填些总分的数据，从第2行开始，到最后一行
for nrow in range(1,sheet.nrows):
    #总分初始值为0
    sum=0
    #提取出每一行的所有数据，从第二列开始，因为第一列没有数字
    for value in sheet.row_values(nrow,1):
        #每次循环+当前的值，就可以获取总分
        sum+=int(value)
    #可以用t=sum(sheet.row_values(nrow,1))获取总分
    #将总分填写到每一行上
    #这样做并不会改变原来的读取的execl文件，只是以缓存的形式保存
    sheet.put_cell(nrow,nc,2,sum,None)

#xlwt,写execl的东西
wbook=xlwt.Workbook()
#获取需要写入的sheet，sheet的名字为sheet.name
wsheet=wbook.add_sheet(sheet.name)
#定义style的格式
sytle=xlwt.easyxf('align:vertical center, horizontal center')
#先遍历所有的行
for row in range(sheet.nrows):
    #再遍历所有的列
    for col in range(sheet.ncols):
        #写入数据到新表格，包括行号、列号、数值、风格
        #cell_value(row,col)是获取之前表格的cell的数值
        wsheet.write(row,col,sheet.cell_value(row,col),sytle)


#save另存为一个xls文件，好像不能xls
wbook.save("output.xls")