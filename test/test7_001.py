# coding:utf-8
import unittest
class Count(unittest.TestCase):
    u'''这是算法类一(简称测试套件)'''
    def test_add(self):
        u'''这是加法用例'''
        self.assertEqual((1+7),8)
        self.assertEqual((8+8),16)
    def test_acc(self):
        u'''这是减法用例'''
        self.assertEqual((9-1),8)
        self.assertEqual((16-8),8)
    def test_aff(self):
        u'''这是乘法用例'''
        self.assertEqual((7*8),56)
        self.assertEqual((9*9),82)
    def test_agg(self):
        u'''这是除法用例'''
        self.assertEqual((64/8),8)
        self.assertEqual((12/2),9)

if __name__ == "__main__":
    # print __name__
    unittest.main()