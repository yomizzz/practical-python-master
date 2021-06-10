import requests
import os
import bs4
from fake_useragent import UserAgent
from time import sleep
from msedge.selenium_tools import Edge
from msedge.selenium_tools import EdgeOptions

# 随机产生请求头
ua = UserAgent(verify_ssl=False, path='fake_useragent.json')

# 当前目录下创建保存音乐的文件夹
path = os.path.join('网易云音乐')
if not os.path.exists(path):
    os.mkdir(path)

# 配置浏览器驱动
options = EdgeOptions()
options.use_chromium = True
options.add_argument('headless')
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ['enable-automaton'])
edge_driver = r"D:\Documents\Downloads\edgedriver_win64\msedgedriver.exe"
name = input('请输入带下载歌名：')
# 初始化browser对象
browser = Edge(options=options, executable_path=edge_driver)

# 获取音乐名称 id 演唱者
def get_name_id_singer(url):
    browser.get(url=url)
    browser.switch_to.frame('g_iframe')
    sleep(1)
    page_text = browser.execute_script("return document.documentElement.outerHTML")
    soup = bs4.BeautifulSoup(page_text, 'html.parser')
    music_names = soup.select("div[class='td w0'] a b")
    music_name = music_names[0].get("title")
    music_ids = soup.select("div[class='td w0'] a")
    music_id = music_ids[0].get("href")
    music_id = music_id.split('=')[-1]
    music_singers = soup.select("div[class='td w1'] a")
    music_singer = music_singers[0].string   # 获取歌手名字
    return music_name, music_id, music_singer

# 请求下载歌曲并保存
def dowload_music(url, song_name, singer):
    headers = {
        "accept-encoding": "gzip",
        "user-agent": ua.random
    }
    resopnse = requests.get(url=url, headers=headers)
    music_data = resopnse.content
    music_path_name = '{}_{}演唱.mp3'.format(song_name, singer)
    music_path = path + '/' + music_path_name
    with open(music_path, 'wb') as f:
        f.write(music_data)
        print(music_path_name, '------>已下载成功！')

# 主函数调用
def main():
    url = 'https://music.163.com/#/search/m/?s=' + name + '&type=1'
    
    # 接收返回的音乐名称 id 演唱者
    music_name, music_id, music_singer = get_name_id_singer(url)
    music_url = 'http://music.163.com/song/media/outer/url?id=' + music_id + '.mp3'
    browser.get(url=music_url)
    sleep(0.5)
    page_text = browser.execute_script("return document.documentElement.outerHTML")
    soup = bs4.BeautifulSoup(page_text, 'html.parser')
    music_source = soup.select("video source")
    
    # 下载歌曲
    source_url = music_source[0].get('src')
    dowload_music(source_url, music_name, music_singer)

if __name__ == '__main__':
    main()
    browser.quit()