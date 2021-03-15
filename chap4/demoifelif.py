# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/11/18 15:35

'''多分支结构，多选一执行'''

s = int(input('请输入考试成绩：'))
if 90 <= s <= 100: # 注意此时的写法
    print('A级。')
elif s >= 80 and s <= 89:
    print('B级。')
elif s >= 70 and s <= 79:
    print('C级。')
elif 60 <= s <= 69:  # 注意此时的写法
    print('D级。')
elif s >= 0 and s <= 59:
    print('不及格。')
else:
    print('成绩输入有误！')