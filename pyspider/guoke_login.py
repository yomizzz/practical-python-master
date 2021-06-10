import requests
import lxml.html

url = 'https://account.guokr.com/sign_in/'
profile_url = 'https://www.guokr.com/settings/profile/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.53'
        }        
requests.packages.urllib3.disable_warnings()  # 忽略跳过SSL验证出现的警告信息

session = requests.Session()
html = session.get(url, headers=headers, verify=False).content # 通过设定verify=False，跳过SSL验证
selector = lxml.html.fromstring(html)
csrf_token = selector.xpath('//form/input/@value')
if not csrf_token:
    print('不能获取csrf_token，无法登录。')
    exit()
csrf_token = csrf_token[0]
captcha_rand = selector.xpath('//form/p/input/@value')
if not captcha_rand:
    print('不能获取captcha_rand，无法登录。')
    exit()
captcha_rand = captcha_rand[0]
captcha_url = selector.xpath('//form/div/img/@src')[0]

image = requests.get(captcha_url, verify=False).content
with open('captcha.png', 'wb') as f:
    f.write(image)

captcha = input('请在这里输入验证码：')
data = {
        'username': '782541451@qq.com',
        'password': '123456',
        'csrf_token': csrf_token,
        'captcha_rand': captcha_rand,
        'captcha': captcha,
        'permanent': 'y'
        }

result = session.post(url, data=data, headers=headers, verify=False).content
profile = session.get(profile_url, headers=headers, verify=False).content.decode()
print(profile)