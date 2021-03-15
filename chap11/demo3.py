# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/10 13:47

lst = [{'rating':[9.7,50],'id':'1292052','type':['犯罪','剧情'],'title':'肖申克的救赎',
        'actors':['蒂姆·罗宾斯','摩根·弗里曼']},
       {'rating':[9.6,50],'id':'1291546','type':['剧情','爱情','同性'],'title':'霸王别姬',
        'actors':['张国荣','张丰毅','巩俐','葛优']},
       {'rating':[9.6,50],'id':'1296141','type':['剧情','犯罪','悬疑'],'title':'控方证人',
        'actors':['秦隆·鲍华','玛琳·黛德丽']}]

name = input('请输入要查询的演员：')

for item in lst: #遍历列表，得到字典项
    act_lst = item.get('actors')
    #print(act_lst)
    for actor in act_lst:
        if name in actor:
            print(name + '出演了' + item.get('title'))
    '''for movie in item: #遍历字典，得到movie是字典中的键
        #print(movie)
        actors = movie['actors']
        #print(actors)
        if name in actors:
            print(name + '出演了' + movie)
        '''