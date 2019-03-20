import unittest
class Math():
    def tell_1(self,a,b):
        return a+b
    def tell_2(self,a,b):
        return a*b

class Tests(unittest.TestCase):
    def setUp(self):
        self.math=Math()
    def test_1(self):
        self.assertEqual(self.math.tell_1(3,4),7)
    def test_2(self):
        self.assertEqual(self.math.tell_2(3,4),12)

if __name__=="__main__":
    unittest.main()
