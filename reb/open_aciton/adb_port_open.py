import os
import random
import json


def Devices():
    devices_list = []
    cmd = "adb devices"
    out = os.popen(cmd)
    list = out.readlines()
    number = len(list)-2
    print("本机adb连接的手机数量是" + str(number))
    adb_list = list[1:-1]
    for i in adb_list:
        device = i.split("\tdevice\n")[0]
        devices_list.append(device)
    return devices_list

def Open_port(device):
    ran_port = str(random.randint(5600,9999))
    print(ran_port)
    port_cmd = "adb -s " + device + " tcpip " + ran_port
    os.system(port_cmd)
    return ran_port

def Ip(devices):
    cmd = "adb -s " + devices +" shell ifconfig wlan0"
    out = os.popen(cmd).readlines()[1]
    try:
        ip = out.split("inet addr:")[1].split("Bcast")[0].strip()
    except:
        ip = out.split("ip")[1].split("mask")[0].strip()
    return ip

def get_size(phoneid):
    wm_cmd = "adb -s " + phoneid + " shell wm size"
    result = os.popen(wm_cmd)
    wm = result.read().split(": ")[1].split("\n")[0]
    wm_w = int(wm.split("x")[0])
    wm_h = int(wm.split("x")[1])
    wm_tuple = (wm_w,wm_h)
    return wm_tuple

def Make_List(adb_list):
    with open('adb.txt','a',encoding='utf-8') as f:
        for id in adb_list:
            ip = Ip(id)
            wm = get_size(id)
            port = Open_port(id)
            remote_id = ip + ":" + port
            name = dict(PhoneId=id,ip=ip,wm_size=wm,port=port,remote_id=remote_id)
            print(name)
            data_str = json.dumps(name)
            f.write(data_str + '\n')
    f.close()


if __name__ == "__main__":
    devices = Devices()
    print(devices)
    Make_List(devices)

