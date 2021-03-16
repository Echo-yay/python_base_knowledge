# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/3/16 18:09

#改需求不修改以写好的参数
#超过既定时间不准玩游戏
#开发封闭原则
def can_play(fn):
    def inner(name,game,*args,**kwargs):
        #print(args)
        #clock = kwargs['clock']
        clock = kwargs.get('clock',23)
        if clock <= 22:
            fn(name,game)
        else:
            print('太晚了，别玩了')
    return  inner

@can_play
def play_game(name,game):
    print('{0}正在玩{1}'.format(name,game))

play_game('echo','王者荣耀',clock = 18)
play_game('john','和平精英')
