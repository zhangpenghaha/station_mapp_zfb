import unittest
import logging
from baseView.baseView import baseView

class myassert(unittest.TestCase,baseView):

    def myEq(self,预期结果,实际结果,模块描述):
        if 预期结果 != 实际结果:
            self.fun_截图(模块描述)
            logging.info("失败!")
            return self.assertEqual(预期结果, 实际结果)
        else:
            logging.info("通过!")
            return self.assertEqual(预期结果, 实际结果)

    def myEq_in(self,预期结果,实际结果,模块描述):
        if 预期结果 in 实际结果:
            self.fun_截图(模块描述)
            logging.info("失败!")
            return self.assertIn(预期结果, 实际结果)
        else:
            logging.info("通过!")
            return self.assertIn(预期结果, 实际结果)

    def myEq_ture( self, 预期结果, 模块描述 ):
        if 预期结果:
            logging.info("通过!")
            return self.assertTrue(预期结果, "test_2_手动添加行程_车次查询")
        else:
            self.fun_截图(模块描述)
            logging.info("失败!")
            return self.assertTrue(预期结果)

