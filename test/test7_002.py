# coding:utf-8
import unittest
class Count(unittest.TestCase):
    '''这是算法类二(简称测试套件)'''
    def test_add(self):
        u'''这是加法测试用例'''
        self.assertEqual((1+7),8)
        self.assertEqual((8+8),16)
    def test_acc(self):
        u'''这是减法测试用例'''
        self.assertEqual((9-1),8)
        self.assertEqual((16-8),8)
    def test_aff(self):
        u'''这是乘法测试用例'''
        self.assertEqual((7*8),56)
        self.assertEqual((9*9),81)
    def test_agg(self):
        u'''这是除法测试用例'''
        self.assertEqual((64/8),8)
        self.assertEqual((12/2),6)

if __name__ == "__main__":
    # print __name__
    unittest.main()