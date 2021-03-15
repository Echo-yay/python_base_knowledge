# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/12/29 16:26

print('apple'>'app') #True
print('apple'>'banana') #False
print('a',ord('a'))
print('b',ord('b'))
print(chr(97),chr(98))

print(ord('李'))
print(chr(26446))

'''==与is的区别
== 比较value
is 比较id
'''
a = b = 10
c = 10

print(a == b)
print(a is b)
print(a == c)
print(a is c)