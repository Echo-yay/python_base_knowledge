# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2020/12/29 17:28

# 编码解码，用于爬虫技术
s = '但愿人长久，千里共婵娟'
#编码
print(s.encode(encoding='GBK')) # GBK一个中文占两个字节
print(s.encode(encoding='UTF-8')) # UTF-8中一个中文占三个字节

#解码
byte1 = s.encode(encoding='GBK')
print(byte1.decode(encoding='GBK'))
byte2 = s.encode(encoding='UTF-8')
print(byte2.decode('UTF-8'))