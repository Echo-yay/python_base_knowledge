# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/12/29 15:01

# 字符串中的大小写转换
print('--------大写---------------')
s = 'hello python'
a = s.upper() #转成大写之后产生新的字符串对象
print(s,id(s))
print(a,id(a))

print('-------小写---------------')
print(s.lower(),id(s.lower()))
print(s,id(s))

print('-------大小转化---------------')
s = 'Hello Python'
b = s.swapcase()
print(s,id(s))
print(b,id(b))

print('-----------题目------------')
s = 'heLLo,python'
c = s.title()
print(c)

print('---------capitalize()----------')
s = 'hEllO pythoN'
d = s.capitalize()
print(d)
