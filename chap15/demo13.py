#encoding=utf-8
# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/15 17:36

#MyContentMgr实现了特殊方法__enter__()和__exit__()，
#称该类遵守了上下文管理器协议，该类对象的实例对象，称为上下文管理器
class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了')

    def show(self):
        print('show方法被调用执行了')
        #print('show方法被调用执行了',1/0)  #无论在上下文处理器中是否产生了异常，exit方法都会被调用

with MyContentMgr() as file:    #相当于file=MyContentMgr()
    file.show()

