# coding:utf-8
import HTMLTestRunner
import unittest
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Greate(unittest.TestCase):
    def test_001(self):
        # 获取当前脚本的真实路径，绝对路径
        # \向右
        self.real_path = os.path.realpath(__file__)
        print self.real_path

        # 获取当前脚本所在的文件夹
        self.dir_path = os.path.dirname(self.real_path)
        print self.dir_path

        # 拼接路径
        file_path = os.path.join(self.dir_path,"test")
        print file_path

        # 加载所有的用例
        # discover方法加载多个用例集合
        self.discover=unittest.defaultTestLoader.discover(start_dir=file_path,
                                                 pattern="test7*.py"
                                                 )

        #指定报告的生成路径和名称
        file_res = os.path.join(self.dir_path,"report\\result.html")
        print file_res

        #以二进制的方式写入并打开报告
        fp=open(file_res,"wb")
        #HTMLTestRunner.HTMLTestRunner()表示HTMLTestRunner模块中的HTMLTestRunner类
        runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                             title=u"算法项目测试报告",
                                             description=u"算法用例执行情况：",
                                             verbosity=2
                                             )
        runner.run(self.discover)


if __name__== "__main__":
    unittest.main()


