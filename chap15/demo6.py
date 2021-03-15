# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/15 17:00

src_file = open('logo.jpg','rb')
target_file = open('copylogo.jpg','wb')
target_file.write(src_file.read())
target_file.close()
src_file.close()