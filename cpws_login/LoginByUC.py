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
from selenium.webdriver import Chrome, ChromeOptions


if __name__ == '__main__':
    driver = uc.Chrome()
    driver.get('https://wenshu.court.gov.cn/website/wenshu/181010CARHS5BS3C/index.html?https://wenshu.court.gov.cn/website/wenshu/181029BPRY8AYR1P/index.html?open=login')
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
    driver.switch_to.frame('contentIframe')
    useranme = driver.find_element_by_xpath('//*[@id="root"]/div/form/div/div[1]/div/div/div/input').send_keys("xxxxxxx")
    time.sleep(5)
    password = driver.find_element_by_xpath('//*[@id="root"]/div/form/div/div[2]/div/div/div/input').send_keys("xxxxxxx")
    time.sleep(5)
    login = driver.find_element_by_xpath('//*[@id="root"]/div/form/div/div[3]/span').click()
    time.sleep(10)
    driver.get("https://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?pageId=95630913fe884718502123ccc06913a9&s8=02")
    time.sleep(10)
    driver.refresh()
    time.sleep(5)
    driver.get("https://wenshu.court.gov.cn/website/wenshu/181107ANFZ0BXSK4/index.html?docId=f527c88abc7440e6b4a0ae46010a5cea")
    time.sleep(10)
    driver.refresh()
    time.sleep(5)

    
    
    

