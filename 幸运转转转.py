import random
import time as t
while True:
    input("回车抽取...")
    num = random.randint(1,20)
    print("3",end="")
    t.sleep(0.5)
    print(".",end="")
    t.sleep(0.5)
    print(".",end="")
    t.sleep(0.5)
    print(".",end="\n")
    print("2",end="")
    t.sleep(0.5)
    print(".",end="")
    t.sleep(0.5)
    print(".",end="")
    t.sleep(0.5)
    print(".",end="\n")
    print("1",end="")
    t.sleep(0.5)
    print(".",end="")
    t.sleep(0.5)
    print(".",end="")
    t.sleep(0.5)
    print(".",end="\n")
    t.sleep(0.5)
    if num == 1:
        a = "1.去找薄弱学科老师，夸老师三个优点，找老师要签名。"
    if num == 2:
        a = "2.当着全班，微笑着吃两片柠檬。"
    if num == 3:
        a = "3.分享一道当天的数学题目。"
    if num == 4:
        a = "4.当面夸奖10位同学的优点。"
    if num == 5:
        a = "5.准备一段100字励志语录分享给大家。"
    if num == 6:
        a = "6.面向全班同学唱一首歌。"
    if num == 7:
        a = "7.正能量表演。"
    if num == 8:
        a = "8.面向全班同学背诵一首诗或一段课文。"
    if num == 9:
        a = "9.擦黑板一天或一周。"
    if num == 10:
        a = "10.课间打扫办公室地面。"
    if num == 11:
        a = "11.给老师们每人接一杯水。"
    if num == 12:
        a = "12.当天所有课前，去办公室接老师来上课。"
    if num == 13:
        a = "13.面壁思过，想出三条改正的方法。"
    if num == 14:
        a = "14.手拉手对视一分钟并拥抱(吵架)。"
    if num == 15:
        a = "15.给班级打扫卫生一次。"
    if num == 16:
        a = "16.练习一页字。"
    if num == 17:
        a = "17.写检讨和反思500字，提出改正措施5条。"
    if num == 18:
        a = "18.讲笑话或做鬼脸，全班超过2/3笑了过关。"
    if num == 19:
        a = "19.做10个俯卧撑或20个蹲起。"
    if num == 20:
        a = "20.当天课上主动举手回答问题5次。"
    print(a)
