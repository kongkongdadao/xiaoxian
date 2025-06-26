from .base_action import *



def KuaishouApp_Open(phone_dict):
    phone_id = phone_dict["PhoneId"]
    execute("am start -n com.kuaishou.nebula/com.yxcorp.gifshow.HomeActivity", phone_id)  # 打开快手极速版
    time.sleep(8)
    print("打开快手极速版，并等待了8秒")

def OpenKuaishouNovel(phone_dict):
    phone_id = phone_dict["PhoneId"]
    execute("am start -n com.kuaishou.kgx.novel/com.kuaishou.novel.MainActivity ", phone_id)  # 打开快手极速版
    time.sleep(8)
    print("打开快手免费小说，并等待了8秒")

def OpenDouyin(phone_dict):
    phone_id = phone_dict["PhoneId"]
    execute("am start -n com.ss.android.ugc.aweme.lite/com.ss.android.ugc.aweme.splash.SplashActivity",phone_id)
    time.sleep(8)
    print("打开抖音极速版，并等待了8秒")

def Douyin_Huoshan_Open(phone_dict):
    phone_id = phone_dict["PhoneId"]
    execute("am start -n com.ss.android.ugc.live/com.ss.android.ugc.aweme.splash.SplashActivity",phone_id)
    time.sleep(8)
    print("打开抖音火山版，并等待了8秒")

def OpenToutiaoApp(phone_dict):
    phone_id = phone_dict["PhoneId"]
    execute("am start -n com.ss.android.article.lite/.activity.SplashActivity",phone_id)#打开头条极速版
    time.sleep(8)
    print("打开头条极速版，并等待了8 秒")

def OpenBaiduApp(phone_dict):
    phone_id = phone_dict["PhoneId"]
    execute("am start -n com.baidu.searchbox.lite/com.baidu.searchbox.MainActivity",phone_id)
    time.sleep(8)
    print("打开百度极速版，并等待了8秒")

def OpenYoushiApp(phone_dict):
    phone_id = phone_dict["PhoneId"]
    execute("am start -n com.ss.android.article.search/com.ss.android.article.news.activity.MainActivity",phone_id)
    time.sleep(8)
    print("打开有柿app,并等待了8秒")


def OpenQimaoApp(phone_dict):
    phone_id = phone_dict["PhoneId"]
    execute("am start -n com.kmxs.reader/.home.ui.HomeActivity",phone_id)
    time.sleep(8)
    print("打开七猫app,并等待了8秒")

def OpenFeiduApp(phone_dict):
    phone_id = phone_dict["PhoneId"]
    execute("am start -n com.yuewen.cooperate.reader.free/com.lechuan.mdwz.ui.activity.NovelMainActivity",phone_id)
    time.sleep(8)
    print("打开飞读app,并等待了8秒")

def OpenHongguoApp(phone_dict):
    phone_id = phone_dict["PhoneId"]
    execute("am start -n com.phoenix.read/com.dragon.read.pages.main.MainFragmentActivity", phone_id)  # 打开快手极速版
    time.sleep(8)
    print("打开快手极速版，并等待了8秒")










