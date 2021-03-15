#encoding=utf-8
# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/18 15:53

#列出指定目录下的所有python文件
import os
path = os.getcwd()  #得到当前目录
lst = os.listdir(path)  #获取当前目录下的所有文件

for filename in lst:
    if filename.endswith('.py'):    #如果filename以.py结尾
        print(filename)