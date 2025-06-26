#!/usr/bin/env python3
from actions.plan_actions import *

import json
import multiprocessing
import argparse


def DouyinVideo(Phone_dict,min):
    phone_id = Phone_dict["PhoneId"]
    wm_size = Phone_dict["wm_size"]
    # novel = [(0.9*wm_size[0],0.888*wm_size[1]),(0.5*wm_size[0],0.5*wm_size[1])]
    video = [(0.5*wm_size[0],0.7*wm_size[1]),(0.5*wm_size[0],0.4*wm_size[1])]
    OpenDouyin(Phone_dict)
    Click(0.5*wm_size[0],0.5*wm_size[1],phone_id) #
    print("点击了一下屏幕正中间，下面开始运行视频滑动")
    VideoWatch(video[0],video[1],min,phone_id)
    time.sleep(5)
    execute("am force-stop com.ss.android.ugc.aweme.lite",phone_id)

def DouyinNovel(Phone_dict,min):
    phone_id = Phone_dict["PhoneId"]
    wm_size = Phone_dict["wm_size"]
    novel = [(0.9*wm_size[0],0.888*wm_size[1]),(0.5*wm_size[0],0.5*wm_size[1])]
    NovelWatch(novel[0],novel[1],180,5,min,phone_id)#小说阅读
    execute("am force-stop com.ss.android.ugc.aweme.lite", phone_id)

def DouyinTest(Phone_dict,min):
    phone_id = Phone_dict["PhoneId"]
    wm_size = Phone_dict["wm_size"]
    novel = [(0.9*wm_size[0],0.888*wm_size[1]),(0.5*wm_size[0],0.5*wm_size[1])]
    OpenDouyin(Phone_dict)
    time.sleep(5)
    Click(0.95*wm_size[0],0.05*wm_size[1],phone_id) #
    time.sleep(3)
    Input("fanqiexiaoshuo",phone_id)
    time.sleep(1)
    Click(0.85*wm_size[0],0.35*wm_size[1],phone_id)
    NovelWatch(novel[0],novel[1],180,5,min,phone_id)#小说阅读


def DouyinShopping(Phone_dict):
    phone_id = Phone_dict["PhoneId"]
    wm_size = Phone_dict["wm_size"]
    for i in range(1000):
        ShoppingWatch(Phone_dict)
        time.sleep(5)
        print("ShoppingWatch程序运行的次数",i+1)
        if i % 4 == 0:
            Click(0.5*wm_size[0],0.78*wm_size[1],phone_id)
        else:
            pass
        time.sleep(5)

def Plan(i,id):
    A5 = get_dict(id)
    # A5["PhoneId"] = A5.pop("remote_id") #远程调试需要修改键值对，否则不需要
    if i == 1:
        Video(A5,130)
    elif i == 6:
        DouyinTest(A5,300)
    elif i == 2:
        Novel(A5,300)
    elif i == 3:
        DouyinShopping(A5)
    elif i == 4:
        DouyinNovel(A5,300)
    elif i == 5:
        Novel(A5,300)  #番茄小说阅读
        KuaishouNovel(A5, 0.55, 0.09)#快手小说阅读
        # Qimao(A5,180)
        DouyinVideo(A5,30) #抖音视频
        TtVideo(A5, 15)
        YoushiApp(A5, 65)
        BaiduVideo(A5,30)
        DouyinVideo(A5,30) #抖音视频
        # TtVideo(A5, 20)
        # BaiduVideo(A5, 30)

def Method(num):
    with open('./adb.txt', 'r') as f:
        lines = f.readlines()
        process_list = []
        for line in lines:
            line = json.loads(line)
            p = multiprocessing.Process(target=Plan,args=(num,line["PhoneId"]))
            process_list.append(p)
            p.daemon = True
            p.start()
        for p in process_list:
            p.join()
    f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--str', help='输入字符串')
    args = parser.parse_args()
    Method(5)





