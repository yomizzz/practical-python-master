'''
作者：夜航船夫
链接：https://zhuanlan.zhihu.com/p/108349901
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- author: uncoverman-*-
# Python3 抓取 bing 主页所有背景图片
import urllib.request
import re
import sys
import os

def get_bing_backphoto():
    # python当前运行的路径里如果没有photos这个文件夹，就新建一个。
    if (os.path.exists('photos') == False):
        os.mkdir('photos')
    for i in range(0,8):
        url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx='+str(i)+'&n=1&nc=1361089515117&FORM=HYLH1'
        html = urllib.request.urlopen(url).read()
        if html == 'null':
            print( 'open & read bing error!')
            sys.exit(-1)
        html = html.decode('utf-8')
        reg = re.compile('"url":"(.*?)","urlbase"',re.S)
        text = re.findall(reg,html)
        for imgurl in text :
            # http://cn.bing.com/th?id=OHR.CorsicaHeart_ZH-CN2795615037_1920x1080.jpg&rf=LaDigue_1920x1080.jpg&pid=hp
            bingimgurl = 'http://cn.bing.com'+imgurl
            right = imgurl.index('&')
            name = imgurl.replace(imgurl[right:],'')
            left = name.index('.')
            imgname = name.replace(name[:left+1],'')
            savepath = 'photos/'+ imgname
            urllib.request.urlretrieve(bingimgurl, savepath)
            print (imgname + ' save success!')

get_bing_backphoto()