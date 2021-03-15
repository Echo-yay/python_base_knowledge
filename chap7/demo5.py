# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/25 20:21

# 字典元素的遍历
scores = {'Echo':100,'Henry':98,'Sarah':90}

for i in scores:
    print(i) #打印key
    print(scores[i]) #打印value，key不存在抛异常
    print(scores.get(i))#打印value