#encoding=utf-8
# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/18 15:42

import os.path
print(os.path.abspath('demo13.py'))
print((os.path.exists('demo13.py')),os.path.exists('demo18.py'))
print(os.path.join('D:\Python','demo13.py'))
print(os.path.split('D:\pycharm\python_learning2\chap15'))
print(os.path.splitext('demo13.py'))
print(os.path.basename("D:\pycharm\python_learning2\chap15\demo13.py"))
print(os.path.dirname('D:\pycharm\python_learning2\chap15\demo13.py'))
print(os.path.isdir('D:\pycharm\python_learning2\chap15\demo13.py'))
