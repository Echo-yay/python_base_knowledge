# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/25 20:00

#键的判断
scores = {'Echo':100,'Herny':98,'John':89}
print('AAA' in scores)
print('AAA' not in scores)

# 字典元素的删除
del scores['Echo'] #删除指定的键值对
print(scores)
scores.clear() #字典元素的清空
print(scores)

# 字典元素的新增
scores['Sarah'] = 100
print(scores)

# 修改元素
scores['Sarah'] = '98'
print(scores)