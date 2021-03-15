# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/17 19:08
# 转义字符
print('hello\nworld') # \ + 转义功能的首字母n --> newline == 换行

print('hello\tworld') # hell占了一个\t，o   占了一个\t
print('helloooo\tworld')

print('hello\rworld') # world把hello覆盖掉，因为先输出hello，再回车，光标回到第一位，打印world

print('hello\bworld') # 退一个格，o被删掉

print('http:\\\\www.baidu.com') # 每两个\出一个

print("老师说：\"大家好。\"")

# 原字符：不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r或R
print(r'hello\nworld')
# 注意事项：最后一个字符不能是反斜杠,但可以是两个反斜杠
print(r'hello\nworld\\')
print(r'hello\nworld')