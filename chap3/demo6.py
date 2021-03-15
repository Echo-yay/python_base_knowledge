# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/17 19:17
#布尔运算符
a,b = 1,2

print("-------------and------------")
print(a == 1 and b == 2)
print(a == 1 and b != 2)
print(a != 1 and b == 2)
print(a != 1 or b != 2)
print("------------or---------------")
print(a == 1 or b == 2)
print(a == 1 or b != 2)
print(a != 1 or b == 2)
print(a != 1 or b != 2)
print("-------------not-----------------")
f1 = True
f2 = False
print(not f1)
print(not f2)

print("-----------in --- not in------------")
s = 'hello world'
print('w' in s)
print('s' in s)
print('w' not in s)
print('s' not in s)