# 性能工具
from timeit import Timer

Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()

# 单元测试模块unittest

import unittest

class TestFunction(unittest.TestCase):
  def test_average(self):
    self.assertEqual(average([20, 30, 70]), 40.0)
    self.assertRaises(ZeroDivisionError, average, [])

unittest.main()
