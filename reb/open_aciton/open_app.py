from reboot.actions.plan_actions import *
from reboot.actions.open_action import *
import os
import time
from reboot01.actions.open_action import OpenQimaoApp, OpenFeiduApp


def Devices():
    devices_list = []
    cmd = "adb devices"
    out = os.popen(cmd)
    list = out.readlines()
    number = len(list)-2
    print("本机adb连接的手机数量是" + str(number))
    for i in list[1:-1]:
        phoneid = i.split("\t")[0]
        wm_cmd = "adb -s " + phoneid + " shell wm size"
        result = os.popen(wm_cmd)
        wm = result.read().split(": ")[1].split("\n")[0]
        name = dict(PhoneId=phoneid,wm_size=wm)
        # print(name)
        devices_list.append(name)
    return devices_list

def OpenKSNovel(phone_dict):
    OpenKuaishouNovel(phone_dict)
def OpenKSVideo(phone_dict):
    KuaishouApp_Open(phone_dict)

def OpenTT(phone_dict):
    OpenToutiaoApp(phone_dict)

def OpenDY(phone_dict):
    OpenDouyin(phone_dict)

def OpenBD(phone_dict):
    OpenBaiduApp(phone_dict)

def OpenYoushi(phone_dict):
    OpenYoushiApp(phone_dict)

def OpenQimao(phone_dict):
    OpenQimaoApp(phone_dict)

def OpenFeidu(phone_dict):
    OpenFeiduApp(phone_dict)


if __name__ == "__main__":
    devices_list = Devices()
    print(devices_list)
    for i in devices_list:
        print(i)
        # OpenQimao(i)
        OpenFeidu(i)
    #     OpenKSNovel(i)
    #     time.sleep(60)
    #     OpenKSVideo(i)
    #     time.sleep(60)
    #     OpenBD(i)
    #     time.sleep(60)
    #     OpenTT(i)
    #     time.sleep(60)
    #     OpenDY(i)

