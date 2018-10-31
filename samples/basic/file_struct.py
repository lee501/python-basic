sound/                          顶层包
      __init__.py               初始化 sound 包
      formats/                  文件格式转换子包
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  声音效果子包
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  filters 子包
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...

导入方式1：
import sound.effects.echo
使用模块中的方法 sound.effects.echo.method

from sound.effects import echo
echo.method

# 如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，
__all__ = ["echo", "surround", "reverse"]
# 那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。