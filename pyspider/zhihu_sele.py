'''
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.53'
    }
url = "http://zhihu.com"
source = requests.get(url, headers=headers).content.decode()
print(source)
'''

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge
from msedge.selenium_tools import EdgeOptions
import time
import random

options = EdgeOptions()
options.use_chromium = True
# options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ['enable-automaton'])
edge_url = r"D:\Documents\Downloads\edgedriver_win64\msedgedriver.exe"
# browser = webdriver.Edge(edge_url)
browser = Edge(executable_path=edge_url, options=options)

url = 'https://www.zhihu.com/#signin'
browser.get(url)
browser.find_element_by_xpath(r'//form/div[1]/div[2]').click()
elem = browser.find_element_by_name('username')
elem.clear()
elem.send_keys('15757175884')
password = browser.find_element_by_name('password')
password.clear()
password.send_keys('33U8cUDrfXuB')
time.sleep(random.uniform(0, 1))
# elem.send_keys(Keys.RETURN) # 模拟键盘回车键
browser.find_element_by_xpath(r'//form/button').click()
input('请移动滑块完成验证，完成后回到这里按任意键继续。')
time.sleep(10)
print(browser.page_source)
# browser.quit()