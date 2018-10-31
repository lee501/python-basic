# -*- coding: utf-8 -*-
# 生成器用于产生数据流
def gen_data_from_file(file_name):
  for line in file(file_name):
    yield line

def gen_word(line):
  for word in (w for w in line.split() if w.stript):
