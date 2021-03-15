#encoding=utf-8
# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/18 16:00
import os
path = os.getcwd()
lst_files = os.walk(path)
#print(lst_files)
for dirpath,dirname,filename in lst_files:
    '''print(dirpath)
    print(dirname)
    print(filename)'''

    #for dir in dirname: #当前目录下的子目录
        #print(os.path.join(dirpath,dir))

    for file in filename:
        print(os.path.join(dirpath,file))
    print('----------------------------------------------')
