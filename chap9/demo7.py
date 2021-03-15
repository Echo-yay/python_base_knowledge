# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/12/29 15:54

# 判断字符串
print('-----------是否是标准字符串---------')
s1 = 'hello python'
print(s1.isidentifier()) #False
s2 = 'hello'
print(s2.isidentifier()) #True
s3 = '安晴'
print(s3.isidentifier()) #True

print('---------是否全为空格----------')
s4 = '\t'
print(s4.isspace())

print('---------全为字母--------------')
s5 = 'abc'
s6 = 'abc123'
s7 = '张三'
print(s5.isalpha())
print(s6.isalpha())
print(s7.isalpha())

print('---------全为十进制数字--------------')
s8 = '184723'
print(s8.isdecimal())
s9 = 'asfd' #罗马数字
print(s9.isdecimal())

print('---------全为数字--------------')
s10 = '1245456'
print(s10.isnumeric())

ss = '1325三'
print(ss.isnumeric())
s11 = '13235scz'
print(s11.isnumeric())

print('---------全为字母和数字--------------')
s12 = '123432rhvubgi'
print(s12.isalnum())
s13 = 'cdfh13^'
print(s13.isalnum())