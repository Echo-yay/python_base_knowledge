#encoding=utf-8
# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/28 13:52

#输出图书信息
#变量名使用下划线连接
#类名首字母大写
filename = 'bookInfo.txt'
book_name = 'Java程序设计教程'
publish = '西安电子科技大学出版社'
pub_date = '2019-02-02'
price = '56.8'
with open(filename,'w',encoding='utf-8') as wfile:
    wfile.write('▶→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→◀\n')
    wfile.write('▷\t\t《')
    wfile.write(book_name)
    wfile.write('》\t\t◁\n')
    wfile.write('▷\t')
    wfile.write(publish)
    wfile.write('\t\t\t◁\n')
    wfile.write('▷\t')
    wfile.write(pub_date)
    wfile.write('\t\t\t\t\t◁\n')
    wfile.write('▷\t')
    wfile.write(price)
    wfile.write('\t\t\t\t\t\t◁\n')
    wfile.write('▶→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→◀\n')

