# 爬取古诗文网关于某个关键词的古诗句，制作飞花令

import requests
from lxml import html

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63'}

def poet_content(keyword, num, url):
    html_data = requests.get(url, headers = headers).text
    selector = html.fromstring(html_data)
    poets = selector.xpath("/html/body/div[2]/div[1]/div[@class='sons']")
    
    for poet in poets:
        title = ''.join(poet.xpath("div[1]/p[1]/a/b//text()")).strip()
        source = ''.join(poet.xpath('div[1]/p[2]//text()'))
        source = ''.join([i.strip() for i in source])
        contents = ''.join(poet.xpath('div[1]/div[@class="contson"]//text()')).strip().replace('\n', '。').replace('？', '。').split('。')
        
        content_lst = []
        for i in contents:
            if keyword in i:
                content = i.strip() + '。'
                content_lst.append(content)
                
        if not content_lst:
            continue
        
        for j in list(set(content_lst)):
            print(num, j)
            print(f'<{title}>', source)
            print('')
            num += 1
    return num
    
if __name__ == '__main__':
    keyword = input('> 请输入关键词：')
    print('')
    num = 1
    
    for i in range( 1, 3):
        url = f'https://so.gushiwen.org/search.aspx?page={i}&value={keyword}'
        num = poet_content(keyword, num, url)

'''
import requests
from lxml import html

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63'}

def poet_content(keyword,num,url):
    html_data = requests.get(url, headers=headers).text
    selector = html.fromstring(html_data)
    poets = selector.xpath("/html/body/div[2]/div[1]/div[@class='sons']")
    for poet in poets:
        title = ''.join(poet.xpath("div[1]/p[1]/a/b//text()")).strip()
        source = ''.join(poet.xpath('div[1]/p[2]//text()'))
        source = ''.join([i.strip() for i in source])
        contents = ''.join(poet.xpath('div[1]/div[@class="contson"]//text()')).strip().replace('\n', '。').replace('？','。').split('。')
        content_lst = []
        for i in contents:
            if keyword in i:
                content = i.strip() + '。'
                content_lst.append(content)
        if not content_lst:
            continue
        for j in list(set(content_lst)):
            print(num, j)
            print(f'<{title}>', source)
            print('')
            num += 1
    return num

if __name__ == '__main__':
    keyword = input('> 请输入关键词: ')
    print('')
    num = 1
    for i in range(1, 3):
        url = f'https://so.gushiwen.org/search.aspx?page={i}&value={keyword}'
        num = poet_content(keyword, num, url)
'''

   
    
    