import threading

# 使用全局dict存放对象，以thread作为key获取对应的对象value
global_dict = {}

def std_thread(name):
  # 实例对象
  std = Student(name)
  # 存放在dict中
  global_dict[threading.current_thread()] = std
  do_task_first()
  do_task_second()

def do_task_first():
  # 根据当前线程查找对象
  std = global_dict[threading.current_thread()]
  pass


 #使用ThreadLocal处理线程局部变量问题
local_school = threading.local()
def process_student():
  # 获取当前线程的student
  student = local_school.student
  print('hi, %s (in %s)' % (student, threading.current_thread().name))

def process_thread(student):
  #绑定ThreadLocal的student
  local_school.student = student
  process_student()

thread1 = threading.Thread(target=process_thread, args=('Lee', ), name='Thread-A')
thread2 = threading.Thread(target=process_thread, args=('Anne', ), name='Thread-B') 
thread1.start()
thread2.start()
thread1.join()
thread2.join()