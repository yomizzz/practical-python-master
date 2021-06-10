"""
在屏幕上显示跑马灯文字。

Version: 0.1
Author: yomi
Date: 2021-04-08
"""

import os 
import time

def main():
    content = '北京欢迎你为你开天辟地……'
    while True:
        # 清理屏幕上的输出
        os.system('clear') # os.system('cls') 
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()