# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/25 20:48

# 列表生成式
items = ['Fruits','Books','Others']
prices = [96,78,85]

dict1 = {item:price for item,price in zip(items,prices)}
print(dict1)
dict2 = {item.upper():price for item,price in zip(items,prices)}
print(dict2)

#当元素个数不相等时，会以元素少的为基准生成字典
items = ['Fruits','Books','Others']
prices = [96,78,85,90,80]
dict3 = {item.upper():price for item,price in zip(items,prices)}
print(dict3)