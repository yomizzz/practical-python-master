import requests

login_url = 'http://exercise.kingname.info/exercise_login'
login_url_success = 'http://exercise.kingname.info/exercise_login_success'

data = {'username': 'kingname',
        'password': 'genius',
        'rememberme': 'Yes'
        }


# 使用Session函数进行登录
session = requests.Session()
before_login = session.get(login_url_success).text
print(before_login)
print('============开始登录============')
session.post(login_url, data=data).text # 这一步登录成功后，session里就带上了包含登录信息的cookie，所以后续再次调用session就会自动登录，因此after_login打印出来的就是成功登录后的网页源代码
after_login = session.get(login_url_success).text
print(after_login)

'''
# 直接用get()和post()方法登录
before_login = requests.get(login_url_success).text
print(before_login)
print('============开始登录============')
requests.post(login_url, data=data).text # 直接用requests.post()不会保存cookie信息，所以后续要再访问该网址，需要重新登录
after_login = requests.get(login_url_success).text
print(after_login)
'''