# -*- coding: utf-8 -*-
import json
d = dict(name='lee', age=20, sex='man')
json.dumps(d) #=>'{"age": 20, "score": 88, "name": "Bob"}'

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)

# json class对象的序列化
class Student(object):
  def __init__(self, name, age, score):
    self.name = name
    self.age = age
    self.score = score

def student_to_dict(stu):
  return {
    name: stu.name,
    age: stu.age
    score: stu.score
  }

s = Student('lee', 20, 90)
json.dumps(s, default=student_to_dict)

# 通用
json.dumps(s, default=lambda obj: obj.__dict__)

# 反序列化
def dict_to_student(d):
  return Student(d['name'], d['age'], d['score'])
  
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
d = json.loads(json_str, object_hook=dict_to_student)     