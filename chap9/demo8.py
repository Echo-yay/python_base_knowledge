# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/12/29 16:11

# 替换与合并

s = 'hello Python!'
print(s,id(s))
print(s.replace('Python','Java'),id(s.replace('Python','Java'))) #不影响原字符
print(s)


s1 = 'hello Python Python Python'
print(s1.replace('Python','Java',2))

lst = ['Echo','Henry','Sarah']
print(s.join(lst))
print(''.join(lst))
tup = ('Echo','Henry')
print(s.join(tup))
print(''.join(tup))

print('#'.join('Echo'))