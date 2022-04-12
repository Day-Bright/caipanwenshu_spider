# -*- coding: UTF-8 -*-

'''
@Product ：VScode
@File    ：LoginByUC.py
@Date    ：2022/01/26 00:21:44
@Author  ：XYJ
@Contact ：1520207872@qq.com
'''

import time
import undetected_chromedriver.v2 as uc
from selenium import webdriver


def waiting_load(page_path, max_time=20):
    "等待路径加载完成"
    for i in range(max_time):
        try:
            loading_completed = driver.find_element_by_xpath(page_path)
            return loading_completed
        except Exception as e:
            i = i - 1
            if i == max_time - 1:
                raise ValueError("路径未找到") from e
            time.sleep(0.5)


if __name__ == '__main__':
    driver = uc.Chrome()
    max_time = 20
    for i in range(max_time):
        try:
            driver.get(
                'https://wenshu.court.gov.cn/website/wenshu/181107ANFZ0BXSK4/index.html?docId=5b4fd193f4b24059a12dae520132f6a2')
            driver.switch_to.frame('contentIframe')
            break
        except Exception as e:
            i = i - 1
            if i == max_time - 1:
                raise ValueError("网页未打开或路径未找到") from e
            # elif i == 10:
            # driver.refresh()
            time.sleep(0.5)
            driver.refresh()
    # time.sleep(1)
    waiting_load(
        '//*[@id="root"]/div/form/div/div[1]/div/div/div/input').send_keys("xxxxx")
    waiting_load(
        '//*[@id="root"]/div/form/div/div[2]/div/div/div/input').send_keys("xxxxx")
    waiting_load('//*[@id="root"]/div/form/div/div[3]/span').click()
    # driver.get("https://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=95630913fe884718502123ccc06913a9&s8=02")
    # time.sleep(10)
    # driver.refresh()
    # time.sleep(5)
    # driver.get("https://wenshu.court.gov.cn/website/wenshu/181107ANFZ0BXSK4/index.html?docId=f527c88abc7440e6b4a0ae46010a5cea")
    # time.sleep(10)
    # driver.refresh()
    # time.sleep(100)
