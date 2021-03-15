# 中国矿业大学（北京）/ 机电硕-6 / ZQT2000405103 / 李天鸽
# 编辑时间：2021/1/14 17:48
import schedule
import time
def job():
    print('3s啦---')

schedule.every(3).seconds.do(job)   #每三秒打印job

while True:
    schedule.run_pending()
    time.sleep(1)   #休眠1s