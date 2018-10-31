# -*- coding: utf-8 -*-
import math

def move(x, y, step, angle=0):
  nx = x + step * math.cos(angle)
  ny = y + step * math.sin(angle)
  return nx, ny

# 求乘机
def power(x, n):
  s = 1
  while n > 0:
    n -= 1
    s = s * x
  return s
  