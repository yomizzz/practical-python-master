import requests
import re
import sys
import os
import json

def get_bing_photos():
	if (os.path.exists('photos') == False):
		os.mkdir('photos')
	for i in range(8):
		headers = {
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.53'
			}
		url = url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx='+str(i)+'&n=1&nc=1361089515117&FORM=HYLH1'
		html = requests.get(url, headers = headers).content.decode()
		if html == 'null':
			print( 'open & read bing error!')
			sys.exit(-1)
		photo_dict = json.loads(html)
		photos = photo_dict['images']
		imgurls = []
		for photo in photos:
			imgurls.append(photo['url'])
		for imgurl in imgurls:
			bingimgurl = 'http://cn.bing.com'+imgurl
			right = imgurl.index('&')
			name = imgurl.replace(imgurl[right:],'')
			left = name.index('.')
			imgname = name.replace(name[:left+1],'')
			savepath = 'photos/'+ imgname
			image = requests.get(bingimgurl, headers = headers).content
			with open(savepath, 'wb') as f:
				f.write(image)
			# urllib.request.urlretrieve(bingimgurl, savepath)
			print (imgname + ' save success!')

get_bing_photos()
