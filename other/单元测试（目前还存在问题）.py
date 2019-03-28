def get_formatted_name(first,last,middle=''):
    if middle:
        full_name = first + ' ' + middle +' ' +last
    else:
        full_name = first + ' '  + last
    return  full_name.title()
import unittest

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis','joplin')
        print(formatted_name)
        self.assertEqual(formatted_name,'Janis Joplin')
        """测试执行代码get_foematted_name,其结果是否与Janis Joplin一致"""
        """assertEqual=将括号内两个参数进行比较"""
    def test_fist_last_middle_name(self):
        formattd_name =get_formatted_name('wolf','amadeus','mozart')
        self.assertEqual(formattd_name,'Wolf Mozart Amadeus')
#两种方法
#方法1
#unittest.main
unittest.main
#方法2
# if __name__=="__main__":
#     unittest.main()