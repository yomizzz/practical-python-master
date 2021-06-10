import requests
import lxml.html
import csv
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.53'}
url = 'https://www.baiten.cn/results/s/%25E5%25AE%2581%25E5%25BE%25B7%25E6%2597%25B6%25E4%25BB%25A3/.html?type=s#/10/1'
source = requests.get(url, headers = headers).content
selector = lxml.html.fromstring(source)
item_list = selector.xpath('//ul/li/h3')

item_dict_list = []
for item in item_list:
	patent_url = item.xpath('a/@href') 
	patent_name = item.xpath('text()') 
	patent_title = item.xpath('a/text()') 
	item_dict = {'patent_name': patent_name[0] if patent_name else '',
				'patent_url': patent_url[0] if patent_url else '',
				'patent_title': patent_title[0] if patent_title else ''}
	
	item_dict_list.append(item_dict)

with open('patent.csv', 'w', encoding='gbk') as f:
	writer = csv.DictWriter(f, fieldnames = ['patent_name',
											'patent_url',
											'patent_title'])
	writer.writeheader()
	writer.writerows(item_dict_list)