import os
import time
import json

def execute(cmd, PhoneId):
    adb_str = "adb -s " + PhoneId + " " + "shell {}".format(cmd)
    # print(adb_str)
    os.system(adb_str)

def Click(x, y, PhoneId):
    cmd = "input tap " + str(x) + " " + str(y)
    execute(cmd, PhoneId)

def Input(keyword,phone_id):
    cmd = "am broadcast -a ADB_INPUT_TEXT --es msg " + keyword
    execute(cmd,phone_id)

def Swipe(x1, y1, x2, y2, swipe_time, PhoneId):  # 滑动
    cmd = "input swipe " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2) + " " + str(swipe_time)
    execute(cmd, PhoneId)

def RollUp(phone_id):
    Swipe(500, 1300, 500, 300, 1000, phone_id)  # 向上翻滚1000
    time.sleep(1)

def RollDown(phone_id):
    Swipe(500, 300, 500, 1300, 1000, phone_id)  # 向下翻滚1000
    time.sleep(1)

def get_dict(ID):
    with open('./adb.txt','r') as f:
        lines = f.readlines()
        try:
            for line in lines:
                phoneid = json.loads(line).get("PhoneId")
                if phoneid == ID:
                    phone_dict = json.loads(line)
                    return phone_dict
                else:
                    print("不是匹配的字典")
        except:
            print("没有找到匹配的字典++++++++++")
