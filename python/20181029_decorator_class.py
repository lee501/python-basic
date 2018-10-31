# 装饰器类
from functools import wraps

class logit(object):
  def __init__(self, logfile='out.log'):
    self.logfile = logfile

  def __call__(self, func):
    @wraps(func)
    def wrapped_function(*args, **kwargs):
      log_info = func.__name__ + " was called"
      print(log_info)
      with open(self.logfile, 'a') as f:
        f.write(log_info + '\n')
      self.notify()
      return func(*args, **kwargs)
    return wrapped_function

  def notify(self):
    #这里不处理别的信息
    pass


# 继承logit的email
class email_logit(logit):
  ''' 一个logit的实现版本，可以在函数调用时发送email给管理员 '''
  def __init__(self, email="admin@admin.com", *args, **kwrags):
    self.email = email
    super(email_logit, self).__init__(*args, **kwargs)

  def notify(self):
    # 发送一封email给self.email
    pass
