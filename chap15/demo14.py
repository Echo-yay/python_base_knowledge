#encoding=utf-8
# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/15 17:47

with open('logo.jpg','rb') as src_file:
    with open('copylogo2.jpg','wb') as target_file:
        target_file.write(src_file.read())