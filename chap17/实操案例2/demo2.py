#encoding=utf-8
# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/28 14:12

#输出金陵十二钗
print('------第一种-----')
name1 = '林黛玉'
name2 = '薛宝钗'
name3 = '贾元春'
name4 = '贾探春'
name5 = '史湘云'
print('1.'+name1)
print('2.'+name2)
print('3.'+name3)
print('4.'+name4)
print('5.'+name5)

print('------第二种-----')
lst_name = ['林黛玉','薛宝钗','贾元春','贾探春','史湘云']
lst_sig = ['1.','2.','3.','4.','5.']
for i in range(5):
    print(lst_sig[i],lst_name[i])

print('------第三种-----')
d = {'1.':'林黛玉','2.':'薛宝钗','3.':'贾元春','4.':'贾探春','5.':'史湘云'}
for  key in d:
    print(key,d[key])

print('------第四种------')
for s,name in zip(lst_sig,lst_name):
    print(s,name)