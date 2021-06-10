"""
直接使用threading模块的Thread类来创建线程,利用多线程来实现文件下载

Version: 0.1
Author: yomi
Date: 2021-05-09
"""

# 使用多线程
from threading import Thread
from random import randint
from time import time, sleep

def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成！耗费了%d秒。' % (filename, time_to_download))

def main():
    start = time()
    t1 = Thread(target=download, args=('Python从入门到住院.pdf',))
    t1.start()
    t2 = Thread(target=download,args=('Peking Hot.avi',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒。' % (end - start))

if __name__ == '__main__':
    main()
