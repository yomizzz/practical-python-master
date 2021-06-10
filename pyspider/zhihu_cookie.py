import requests

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5,ja;q=0.4,da;q=0.3',
    'Cookie': '_zap=4903d907-de69-4709-be64-37717027d301; d_c0="AHDWvkY8mBKPTv3wb95h7D9Agl7XKFExYrU=|1612233993"; _xsrf=93AoNDCg626yP6qrUnty3NW2ePPbHwWO; captcha_session_v2="2|1:0|10:1615360651|18:captcha_session_v2|88:Ykp2N2RROG1jTUt6SXcwT1cwck1JSHBGampWa1ZGRnlWVDZtbmc5WGYwZjFOaFQzaklPMldjVlIvWWQ0eWM4dg==|4ba92a679453722800be8f47f3c081f3409233d34e5439a4d0038c5faff728f2"; SESSIONID=6fK4Aq7wHX28vXTTu0q2O87li0oRlOJtWpwjMr9HhRX; JOID=Vl0XAkJyTEtS23eVf3dgnswm-wlrRS0DbpcHpQs3FX5ppSLALPg6CDfXcZF0Kkj-502a6EhDAOp0_vzt7eV-CBo=; osd=UV8VB0t1TklX0nCXfXJpmc4k_gBsRy8GZ5AFpw4-EnxroCvHLvo_ATDVc5R9LUr84kSd6kpGCe12_Pnk6ud8DRM=; captcha_ticket_v2="2|1:0|10:1615360672|17:captcha_ticket_v2|244:eyJhcHBpZCI6IjIwMTIwMzEzMTQiLCJyZXQiOjAsInRpY2tldCI6InQwMzhSREZFaFVCWElLYWwwaFVLV2NWS251OV9uMmpwMXdmcXNrLWJwVzJqUkJWemkxb1NRMTlNRmpjbHZFeDkxZjVoR0dtX2RZelIxQUtIOTJXUHN5eWREbTFET3FHcXdDdG43cElIclp3dVNYbFg2WVBWcTZXcncqKiIsInJhbmRzdHIiOiJAWnVtIn0=|87bf90e8fac71c00f7248b6558144c8cf8bb3325e99361001c75ec5b6e8abe1b"; z_c0="2|1:0|10:1615360672|4:z_c0|92:Mi4xaEFzZUFBQUFBQUFBY05hLVJqeVlFaVlBQUFCZ0FsVk5vTUExWVFCUXcwSTlfQ1QtckY4b3Q2YkF5bjZodk11VVBR|f4425f22b300d9b77a2fa8ccafb3418c70d469a12f75e8550edaa99cd849c209"; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1615337782,1615344560,1615360651,1615363567; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1615363759; KLBRSID=0a401b23e8a71b70de2f4b37f5b4e379|1615363759|1615360650',
    'DNT': '1',
    'Referer': 'https://www.zhihu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45'
}

session = requests.Session()
url = 'https://www.zhihu.com'
source = session.get(url, headers=headers, verify=False).content.decode()
print(source)