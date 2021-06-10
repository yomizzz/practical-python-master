import re
import json
import requests

class LetvSpider(object):
	COMMENT_URL = 'http://api-my.le.com/vcm/api/list?jsonp=jQuery19106467665677354655_1614395490647&type=video&rows=20&page=1&sort=&cid=2&source=1&xid={xid}&pid={pid}&ctype=cmt%2Cimg%2Cvote&listType=1&_=1614395490652'
	HEADERS = {
			'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.53'
			}
	def __init__(self, url):
		self.necessary_info = {}
		self.url = url
		self.get_necessary_id()
		self.get_comment()

	def get_source(self, url, headers):
		return requests.get(url, headers).content.decode()

	# 通过浏览器的检查功能找到评论区域对应的异步加载文件，发现对应的请求url中有xid和pid两项
	# 先获取页面源代码中的xid和pid对应的值
	def get_necessary_id(self):
		source = self.get_source(self.url, self.HEADERS)
		vid = re.search('vid: (\d+)', source).group(1)
		pid = re.search('pid: (\d+)', source).group(1)
		self.necessary_info['xid'] = vid
		self.necessary_info['pid'] = pid

	def get_comment(self):
		url = self.COMMENT_URL.format(xid = self.necessary_info['xid'],
										pid = self.necessary_info['pid'])
		source = self.get_source(url, self.HEADERS)
		source_json = source[source.find('{"'): -1]
		comment_dict = json.loads(source_json)
		comments = comment_dict['data']
		for comment in comments:
			print(f'发帖人: {comment["user"]["username"]}, 评论内容：{comment["content"]}')

if __name__ == '__main__':
	spider = LetvSpider('http://www.le.com/ptv/vplay/72243334.html')