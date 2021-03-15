# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/25 19:54

# 获取字典中的元素
scores = {'Echo':100,'Henry':89,'Sarah':56}
print(scores)

'''使用[]'''
print(scores['Echo'])
#print(scores['aaa']) #KeyError: 'aaa'

'''使用scores.get()'''
print(scores.get('Echo'))
print(scores.get('aaa')) #None
print(scores.get('bbb',99)) # 99是在查找不存在的剪纸时给出的默认值