# 简单的示例
try:
  file = open('demo.txt', 'rb')
except IOError as e:
  print("a IO error occured {}".format(e.args[-1]))

# 处理多个异常

try:
  file = open('demo.txt', 'rb')
except EOFError as e:
  print()
  raise e
except IOError as e:
  print()
  raise e
finally:
  print()

# try/else

try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
   # 这里的代码只会在try语句里没有触发异常时运行,
    # 但是这里的异常将 *不会* 被捕获
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    print('This would be printed in every case.')
