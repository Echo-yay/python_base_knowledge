#encoding=utf-8
# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/18 16:20

# 向文件输出：奋斗成就更好的你

'''1.使用print方式进行输出（输出的目的地是文件）'''
fp = open('D:/pycharm/输出数据/print/a.txt','w')
print('奋斗成就更好的自己',file=fp)
fp.close()

'''2.使用文件的读写操作'''
with open('D:/pycharm/输出数据/print/a.txt','a+') as file:
    file.write('奋斗成就更好的自己！')