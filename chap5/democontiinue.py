# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/24 13:38

'''输出1到50中5的所有倍数'''
for i in range(1,51):
    if not bool(i%5):
        print(i)

print('------------continue-------------')
for i in range(1,51):
    if i%5 !=0:
        continue
    print(i)
