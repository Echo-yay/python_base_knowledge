# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/25 20:13

# 获取字典视图的三个方法
scores = {'Echo':100,'Henry':89,'Sarah':56}

# 获取所有键
keys = scores.keys()
print('keys：',keys,type(keys))
print(list(keys)) #将所有键组成的视图转为列表

# 获取所有值
values = scores.values()
print('values：',values,type(values))
print(list(values))

# 获取所有的键值对
items = scores.items()
print('items：',items,type(items))
print(list(items)) #转换为列表之后的元素叫元组