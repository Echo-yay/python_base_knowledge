# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/10 14:45

#print(10/0)

import traceback
try:
    print('--------------------')
    print(10/0)
except:
    traceback.print_exc()