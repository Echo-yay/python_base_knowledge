#encoding=utf-8
# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/18 15:20
import os
print(os.getcwd())

lst = os.listdir('../chap15')   #..推出到上一层
print(lst)

#os.rmdir('newdir')

#os.mkdir('newdir')

#os.removedirs('A/B/C')

#os.makedirs('A/B/C')

os.chdir('D:\pycharm\python_learning2\chap15')
print(os.getcwd())