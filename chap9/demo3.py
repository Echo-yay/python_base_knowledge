# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/12/28 18:01

# 字符串的查询
s = 'hello,hello'
print(s.index('lo')) #3
print(s.find('lo'))  #3
print(s.rindex('lo')) #9
print(s.rfind('lo')) #9

#print(s.index('k')) #ValueError: substring not found
print(s.find('k'))  #-1
#print(s.rindex('k')) #ValueError: substring not found
print(s.rfind('k')) #-1