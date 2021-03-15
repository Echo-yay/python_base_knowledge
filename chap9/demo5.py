# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/12/29 15:12

# 字符串对齐方法

print('---------居中对齐---------')
s = 'hello,Python'
print(s.center(20,'*'))

print('---------左对齐------------')
s = 'hello,Python'
print(s.ljust(20,'$'))
print(s.ljust(20)) # 填充符不写用默认使用空格填充
print(s.ljust(10,'$')) #对齐长度小于原字符长度时，返回原字符

print('---------右对齐------------')
print(s.rjust(20,'#'))
print(s.rjust(20))
print(s.rjust(10,'#'))

print('--------0填充--------------')
print(s.zfill(20))
print(s.zfill(10))
print('-8990'.zfill(20)) #0会添加到-后面数字前面