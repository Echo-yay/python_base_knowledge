# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/24 14:09

'''流程控制语句break与continue在二重循环中的使用'''
for i in range(5):
    for j in range(1,11):
        if j%2 == 0:
             break
        print(j,end='\t')
    print()

for i in range(5):
    for j in range(1,11):
        if j%2 == 0:
            continue
        print(j,end='\t')
    print()