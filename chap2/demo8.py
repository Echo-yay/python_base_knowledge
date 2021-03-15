# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/17 19:11

name = 'Echo'
age = 21

print(type(name),type(age))

# 类型不同不可链连接
# print("我叫"+name+"，今年"+age+"岁。")  报错
print("我叫"+name+"，今年"+str(age)+"岁。")

print('---------str()将其他类型转化成str类型---------')
a = 10
b = 18.2
c = False
print(type(a),type(b),type(c))
print(str(a),type(str(a)))
print(str(b),type(str(b)))
print(str(c),type(str(c)))

print('---------int()将其他类型转化成int类型---------')
# 字符串必须是整数数字串，否则只能转换整数部分
s1 = '11'
f1 = 13.2
s2 = '32.4'
b1 = False
s3 = 'Hello'
print(type(s1),type(f1),type(s2),type(b1),type(s3))

print('s1:',int(s1),type(int(s1))) # 可
print('f1:',int(f1),type(int(f1)))
#print('s2:',int(s2),type(int(s2))) # 不可，报错
print('b1:',int(b1),type(int(b1))) # 可
#print('s3:',int(s3),type(int(s3)))

print('---------float()将其他类型转化成float类型---------')

s1 = '11.88'
s2 = '32'
b1 = False
s3 = 'Hello'
i = 98
print(type(s1),type(s2),type(b1),type(s3),type(i))

print('s1:',float(s1),type(float(s1))) #可
print('s2:',float(s2),type(float(s2))) #可
print('b1:',float(b1),type(float(b1))) #可
#print('s3:',float(s3),type(float(s3))) 报错
print('i:',float(i),type(float(i))) #可