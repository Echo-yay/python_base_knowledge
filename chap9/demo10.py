# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/12/29 16:40
# 字符串的切片

s = 'hello,Python'
s1 = s[:5]
print('s1',s1)
s2 = s[6:]
print('s2',s2)
s3 = '~'
s4 = s1+s3+s2
print('s4',s4)

print('s',id(s))
print('s1',id(s1))
print('s2',id(s2))
print('s3',id(s3))
print('s4',id(s4))

print('-------------切片[start:end:step]--------------')
s = '0123456789'
print(s[1:7:2])
print(s[::3])
print(s[::-1])
print(s[-6::1])