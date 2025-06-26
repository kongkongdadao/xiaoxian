import os
import time
import json

with open('adb.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        cmd = "adb connect " + json.loads(line).get("remote_id")
        print(cmd)
        try:
            os.system(cmd)
        except Exception as e:
            print(e)

# time.sleep(10)
#
# try:
#     cmd_run = "nohup python3 ./main.py -n > /dev/null 2>&1 &"
#     os.system(cmd_run)
# except Exception as e:
#     print(e)

