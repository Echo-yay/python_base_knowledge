#coding:utf-8
# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/15 17:31
print(type(open('a.txt','r')))
with open('a.txt','r') as file:
    print(file.read())