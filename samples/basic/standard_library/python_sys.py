# 脚本经常调用的命令行工具，以列表的形式存储在sys的argv变量当中

# 例如在命令行中执行 "python demo.py one two three" 后可以得到以下输出结果:
import sys

sys.argv

#>>['demo.py', 'one', 'two', 'three']

# sys 还有 stdin，stdout 和 stderr 属性，即使在 stdout 被重定向时，后者也可以用于显示警告和错误信息。

sys.stderr.write('Warning, log file not found starting a new one\n')

# 大多脚本的定向终止都使用 "sys.exit()"

