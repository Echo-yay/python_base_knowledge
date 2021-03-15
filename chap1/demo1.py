# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/17 19:07
# 输出数字
print(520)
print(98.5)

# 输出字符串
print('hello world')
print("hello world")

# 输出含有运算符的表达式
print(3+1)

# 将数据输出到文件中。
# 注意点：1.指定盘符要存在；2.使用file = **，例如file = fp
fp = open('D:/pycharm/输出数据/print/text.txt','a+') # 'a+'意思是：若文件不存在则在指定位置创建，若存在，则在文件中内容后面继续追加
print('hello world',file = fp)
fp.close()

# 不进行换行输出（输出内容在一行中）
print('hello','world','Python')