from .open_action import *

import random
from datetime import datetime


def ShoppingWatch(Phone_dict):
    phone_id = Phone_dict["PhoneId"]
    wm_size = Phone_dict["wm_size"]
    shop = [(0.5 * wm_size[0], 0.7 * wm_size[1]), (0.5 * wm_size[0], 0.4 * wm_size[1])]
    start_time = datetime.now()
    print("逛街的连续动作开始运行")
    for i in range(0,9):
        Swipe(shop[0][0],shop[0][1],shop[1][0],shop[1][1],300,phone_id)
        print(phone_id + "动作是向下滑动")
        time.sleep(5)
    for i in range(0,9):
        Swipe(shop[1][0], shop[1][1], shop[0][0], shop[0][1], 300, phone_id)
        print(phone_id + "动作是向上滑动")
        time.sleep(5)
    print("逛街的连续动作结束一次运行")
    end_time = datetime.now()
    run_time = (end_time - start_time).seconds
    print("运行一次的时间是：" + str(run_time) + "单位是秒")

def Shopping(Phone_dict):
    phone_id = Phone_dict["PhoneId"]
    for i in range(1000):
        ShoppingWatch(Phone_dict)
        wm_size = Phone_dict["wm_size"]
        print("ShoppingWatch程序运行的次数",i+1)
        if i % 4 == 0:
            Click(0.50*wm_size[0],0.75*wm_size[1],phone_id)
        else:
            pass

def NovelWatch(down,up,watch,interval,swipe_time,phone_id):
    seconds = int(watch * 60 / interval)
    for i in range(0,seconds):
        Swipe(down[0],down[1],up[0],up[1],swipe_time,phone_id)
        read_time = i * interval / 60
        print(phone_id + "阅读了" + str(read_time) + "分钟")
        time.sleep(interval)

def Novel(Phone_dict,min):
    phone_id = Phone_dict["PhoneId"]
    wm_size = Phone_dict["wm_size"]
    novel = [(0.9*wm_size[0],0.888*wm_size[1]),(0.4*wm_size[0],0.888*wm_size[1])]
    NovelWatch(novel[0],novel[1],170,5,min,phone_id)

def VideoWatch(down_point,up_point,minute,PhoneId):
    min = int(minute*60/5)
    for i in range(1,min):
        Swipe(down_point[0],down_point[1],up_point[0],up_point[1],200,PhoneId)
        rest_time_list = [10,11,7,5,4,6,9]
        read_time = i * 9 / 60
        print(PhoneId + "的浏览视频时间" + str(read_time) + "分钟")
        rest_time = random.choice(rest_time_list)
        time.sleep(rest_time)

def Video(phone_dict,min):
    phone_id = phone_dict["PhoneId"]
    wm_size = phone_dict["wm_size"]
    video = [(0.5*wm_size[0],0.6*wm_size[1]),(0.5*wm_size[0],0.3*wm_size[1])]
    VideoWatch(video[0],video[1],min,phone_id)

def AdWatch(ad_point, waite_time, watch_time, PhoneId):  # x,y 进入坐标，waite_time 观看时间，watch_time,观看次数，a,b退出坐标
    for i in range(0, watch_time):
        Click(ad_point[0][0], ad_point[0][1], PhoneId)  # 进入广告页面
        time.sleep(waite_time)  # 观看广告
        Click(ad_point[1][0], ad_point[1][1], PhoneId)  # 点击退出
        print("第" + str(i) + "次观看广告完毕")
        time.sleep(3)
    print("观看了" + str(i) + "次广告")

def Search(get_in, search_point,get_out,key_word,phone_id):
    Click(get_in[0],get_in[1],phone_id)
    time.sleep(3)
    keyword = random.choice(key_word)
    Input(keyword,phone_id)
    time.sleep(10)
    Click(search_point[0],search_point[1],phone_id)
    for i in range(0, 6):
        RollUp(phone_id)
        time.sleep(3)
    Click(get_out[0],get_out[1],phone_id)
    time.sleep(1)
    Click(get_out[0],get_out[1],phone_id)
    time.sleep(5)
    RollUp(phone_id)
    time.sleep(5)
    RollUp(phone_id)


# def Living(phone_dict,box_y):
#     phone_id = phone_dict["PhoneId"]
#     wm_size = phone_dict["wm_size"]
#     y = box_y * wm_size[1]
#     Click(0.9*wm_size[0],y,phone_id)#点击进入宝箱
#     time.sleep(3)
#     for i in range(0,9):
#         if i < 4:
#             x = (i + 1 ) * (wm_size[0]/5.5)
#             Click(x,0.45*wm_size[1],phone_id)#点击宝箱
#             time.sleep(2)
#             Click(0.5*wm_size[0],0.725*wm_size[1],phone_id)#收取金币
#             time.sleep(2)
#             Click(0.5*wm_size[0],0.3*wm_size[1],phone_id)#回到直播见
#             time.sleep(2)
#             time.sleep(180)#观看直播
#         else:
#             Click(0.5*wm_size[0],0.725*wm_size[1],phone_id)
#             time.sleep(2)
#             Click(0.5 * wm_size[0], 0.725 * wm_size[1], phone_id)  # 收取金币
#             time.sleep(2)
#             Click(0.5 * wm_size[0], 0.3 * wm_size[1], phone_id)  # 回到直播见
#             time.sleep(2)
#             time.sleep(180)#观看直