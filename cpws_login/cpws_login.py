# -*- coding: UTF-8 -*-

"""
@Project ：website_login 
@Product ：PyCharm
@File    ：cpws_login.py
@Date    ：2021/10/6 22:04 
@Author  ：XYJ
@Contact ：1520207872@qq.com
"""
import execjs
import requests
import web_heardes.cpws_heardes as heardes


def login(username, encrypt_key):
    """
    返回操作成功即登录成功
    :param username:
    :param encrypt_key:
    :return:
    """
    session = requests.Session()
    login_url = "https://account.court.gov.cn/api/login"
    data = {
        "username": username,
        "password": encrypt_key,
        "appDomain": "wenshu.court.gov.cn"
    }
    response = session.post(url=login_url, data=data, headers=heardes.cpws_heardes)
    print(response.text)
    # print(session.cookies.get_dict())
    # main_url = "https://wenshu.court.gov.cn/website/wenshu/181029CR4M5A62CH/index.html?#"
    # main_response = session.get(url=main_url,headers=heardes.main_heardes)
    # print(main_response.text)


def getEncryptKey(password):
    file = "web_js/cpws_login.js"
    ctx = execjs.compile(open(file, encoding="utf-8").read())
    js = 'getpwd("{password}")'.format(password=password)
    encrypt_key = ctx.eval(js)
    return encrypt_key


if __name__ == '__main__':
    encrypt_key = getEncryptKey("Cp911922@")
    login("15776690679", encrypt_key)
