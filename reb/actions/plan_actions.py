import time

from .continu_action import *


def Hongguo(Phone_dict):
    OpenHongguoApp(Phone_dict)
    print("打开了红果")


def KuaishouNovel(Phone_dict,ad_y,ad_out):
    phone_id = Phone_dict["PhoneId"]
    wm_size = Phone_dict["wm_size"]
    novel = [(0.93*wm_size[0],0.88*wm_size[1]),(0.6*wm_size[0],0.88*wm_size[1])]
    ad_point = [(0.8*wm_size[0],ad_y*wm_size[1]), (0.08*wm_size[0],ad_out*wm_size[1])]
    #快手免费小说
    OpenKuaishouNovel(Phone_dict)  # 打开快手极速版
    print("打开了快手免费小说")
    time.sleep(10)
    Click(0.5*wm_size[0],0.95*wm_size[1],phone_id)#点击进入福利界面
    print("进入福利界面")
    time.sleep(5)
    # 广告任务
    # AdWatch(ad_point,32,10,phone_id)#看广告
    Click(0.1*wm_size[0],0.95*wm_size[1],phone_id)#点击进入书城
    time.sleep(5)
    Click(0.2*wm_size[0],0.85*wm_size[1],phone_id)
    NovelWatch(novel[0], novel[1], 260, 5, 300, phone_id)
    execute("am force-stop com.kuaishou.kgx.novel",phone_id)#退出快手免费小说
    time.sleep(3)

def TtVideo(Phone_dict,min):
    phone_id = Phone_dict["PhoneId"]
    wm_size = Phone_dict["wm_size"]
    OpenToutiaoApp(Phone_dict)
    time.sleep(6)
    flush_time = int(min / 5)
    for i in range(0, flush_time):
        Click(0.1 * wm_size[0], 0.95 * wm_size[1], phone_id)
        print("点击主页，刷新主要内容")
        Video(Phone_dict, 5)
        Click(0.24 * wm_size[0], 0.95 * wm_size[1], phone_id)
        print("点击视频，刷新视频")
        Video(Phone_dict, 5)
        print("运行一次的时间是十分钟，运行的次数是" + str(i + 1))


def TtRead(phone_dict,min):
    phone_id = phone_dict["PhoneId"]
    wm_size = phone_dict["wm_size"]
    novel_action = phone_dict["toutiao"]
    novel = [(0.93*wm_size[0],0.88*wm_size[1]),(0.6*wm_size[0],0.88*wm_size[1])]
    OpenToutiaoApp(phone_dict)
    time.sleep(10)

    Click(0.25*wm_size[0],0.95*wm_size[1],phone_id) #点击主页
    time.sleep(3)
    Click(novel_action[0][0]*wm_size[0], novel_action[0][1]*wm_size[1], phone_id)#点击免费小说书架
    # print(novel_action[0][0]*wm_size[0], novel_action[0][1]*wm_size[1],"点击免费小说")
    time.sleep(8)
    Click(novel_action[1][0]*wm_size[0],novel_action[1][1]*wm_size[1],phone_id)#点击书本
    print("点击书本")
    time.sleep(5)
    NovelWatch(novel[0], novel[1], 190, 5, min, phone_id)
    execute("am force-stop com.ss.android.article.lite",phone_id)


def Douyinhuoshan(Phone_dict,min):
    phone_id = Phone_dict["PhoneId"]
    wm_size = Phone_dict["wm_size"]
    video = [(0.5*wm_size[0],0.7*wm_size[1]),(0.5*wm_size[0],0.3*wm_size[1])]
    Douyin_Huoshan_Open(Phone_dict)
    time.sleep(10)
    VideoWatch(video[0],video[1],min,phone_id)

def BaiduVideo(Phone_dict,min):
    phone_id = Phone_dict["PhoneId"]
    wm_size = Phone_dict["wm_size"]
    novel = [(0.9*wm_size[0],0.888*wm_size[1]),(0.5*wm_size[0],0.6*wm_size[1])]
    video = [(0.5*wm_size[0],0.7*wm_size[1]),(0.5*wm_size[0],0.3*wm_size[1])]
    OpenBaiduApp(Phone_dict)
    time.sleep(8)
    flush_time = int(min / 5)
    for i in range(0, flush_time):
        Click(0.1 * wm_size[0], 0.95 * wm_size[1], phone_id)
        print("点击主页，刷新主要内容")
        Video(Phone_dict, 5)
        Click(0.24 * wm_size[0], 0.95 * wm_size[1], phone_id)
        print("点击视频，刷新视频")
        time.sleep(5)
        Click(0.5*wm_size[0],0.5*wm_size[1],phone_id)# 点击视频中间
        Video(Phone_dict, 5)
        print("运行一次的时间是十分钟，运行的次数是" + str(i + 1))

def BaiduRead(Phone_dict,min):
    phone_id = Phone_dict["PhoneId"]
    wm_size = Phone_dict["wm_size"]
    novel = [(0.9*wm_size[0],0.888*wm_size[1]),(0.5*wm_size[0],0.6*wm_size[1])]
    OpenBaiduApp(Phone_dict)
    time.sleep(8)
    Click(0.75 * wm_size[0], 0.95 * wm_size[1], phone_id)  # 进入小说推荐页
    time.sleep(10)
    Click(0.5 * wm_size[0], 0.25 * wm_size[1], phone_id)  # 进入书本
    time.sleep(10)
    Click(0.2*wm_size[0],0.9*wm_size[1],phone_id) #点击书页右上角一下，
    NovelWatch(novel[0], novel[1], 190, 5, min, phone_id)    # 开始读书
    time.sleep(3)
    execute("am force-stop com.baidu.searchbox.lite",phone_id)#退出百度
    time.sleep(3)


def YoushiApp(Phone_dict,min):
    phone_id = Phone_dict["PhoneId"]
    wm_size = Phone_dict["wm_size"]
    OpenYoushiApp(Phone_dict)
    time.sleep(6)
    flush_time = int(min/5)
    for i in range(0,flush_time):
        Click(0.1 * wm_size[0], 0.95 * wm_size[1], phone_id)
        print("点击主页，刷新主要内容")
        Video(Phone_dict,5)
        Click(0.24*wm_size[0],0.95*wm_size[1],phone_id)
        print("点击视频，刷新视频")
        Video(Phone_dict,5)
        print("运行一次的时间是十分钟，运行的次数是" + str(i+1))


def Kuaishou(Phone_dict):
    phone_id = Phone_dict["PhoneId"]
    wm_size = Phone_dict["wm_size"]
    novel = [(0.9*wm_size[0],0.888*wm_size[1]),(0.5*wm_size[0],0.888*wm_size[1])]
    video = [(0.5*wm_size[0],0.7*wm_size[1]),(0.5*wm_size[0],0.3*wm_size[1])]
    execute("am start -n com.kuaishou.nebula/com.yxcorp.gifshow.HomeActivity", phone_id)  # 打开快手极速版
    # time.sleep(5)
    # VideoWatch(video[0], video[1], 30, phone_id)  #
    # Shopping(Phone_dict)
    NovelWatch(novel[0], novel[1], 190, 6, 300, phone_id)
    Shopping(phone_id)

def Qimao(Phone_dict,min):
    phone_id = Phone_dict["PhoneId"]
    wm_size = Phone_dict["wm_size"]
    novel = [(0.9*wm_size[0],0.8*wm_size[1]),(0.4*wm_size[0],0.6*wm_size[1])]
    OpenQimaoApp(Phone_dict)
    time.sleep(10)
    Click(0.5*wm_size[0],0.68*wm_size[1],phone_id)
    print("点击一下，关闭广告弹窗")
    Click(0.5*wm_size[0],0.68*wm_size[1],phone_id)
    time.sleep(5)
    print("点击进入书本页面")


    NovelWatch(novel[0], novel[1], min, 5, 300, phone_id)
    execute("am force-stop com.kmxs.reader/.home.ui.HomeActivity",phone_id)#退出快手免费小说
    time.sleep(3)
