# -*- coding: UTF-8 -*-

'''
@Product ：VScode
@File    ：cookie_test.py
@Date    ：2022/01/26 00:21:44
@Author  ：XYJ
@Contact ：1520207872@qq.com
'''


    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument(
    #     'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')
    # driver = Chrome('driver\chromedriver.exe', options=chrome_options)
    # with open('stealth.min.js') as f:
    #     js = f.read()
    # driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    #     "source": js
    # })

import time

import undetected_chromedriver.v2 as uc


from selenium.webdriver import Chrome, ChromeOptions

    # driver.delete_all_cookies()
    # cookie = {'HM4hUBT0dDOn443S': 'gdcqG_gsP90el91HFaC_6Ppc3yxjwzNw7eldKW',
    #           'SESSION': 'e50fa580-474f-4611-8e02-87c2dd641e0a',
    #           'wzws_reurl':'L3dlYnNpdGUvd2Vuc2h1L2ltYWdlcy9iZ18wMi5wbmc',
    #           'UM_distinctid': '17f64de033f3b8-05310c5e9d4d9c-56171d58-144000-17f64de0340a2c',
    #           'HM4hUBT0dDOn443T': '4W87dU1QmspPYtxoSDrli1Vj7DckZphDdunR5MVJBI7A',
    #           'HM4hUBT0dDOnenable': 'true',
    #           'CNZZDATA1278108394': "1555888666-1646654977-https%253A%252F%252Fwenshu.court.gov.cn%252F%7C1646654977",
    #           '_bl_uid': 'jRl3j0wjgXyt27oyw977leLsq2hp',
    #           'HOLDONKEY': 'ODBmMDBiNWItYmE5Ni00MThjLWE0YmItZDkxZTRjZTNjYjc1',
    #           }
    # cookie_list = []
    # for key in cookie:
    #     cookie_dict = {'name': key,
    #                    'value': cookie[key],
    #                    }
    #     cookie_list.append(cookie_dict)
    # for i in cookie_list:
    #     # print(i, type(i))
    #     driver.add_cookie(i)
    # # print('-'*30)
    # driver.get("https://wenshu.court.gov.cn/website/wenshu/181107ANFZ0BXSK4/index.html?docId=f527c88abc7440e6b4a0ae46010a5cea")
    # time.sleep(1000)
    # driver.refresh()

if __name__ == '__main__':
    
    # uc.TARGET_VERSION = 91
    
    # uc.install(
    #     executable_path='driver\chromedriver.exe',
    # )
#     uc.TARGET_VERSION = 91
    driver = uc.Chrome()
#     # chrome_options.add_argument("--headless")
    # chrome_options.add_argument(
    #     'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')
    # driver = Chrome('driver\chromedriver.exe', options=chrome_options)
    # with open('stealth.min.js') as f:
    #     js = f.read()
    # driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    #     "source": js
    # })
    driver.get('https://wenshu.court.gov.cn/website/wenshu/181010CARHS5BS3C/index.html?https://wenshu.court.gov.cn/website/wenshu/181029BPRY8AYR1P/index.html?open=login')
    time.sleep(5)
    driver.refresh()
    time.sleep(5)
    driver.switch_to.frame('contentIframe')
    
    # wait('//*[@id="root"]/div/form/div/div[1]/div/div/div/input')
    
    useranme = driver.find_element_by_xpath('//*[@id="root"]/div/form/div/div[1]/div/div/div/input').send_keys("15776690679")
    time.sleep(5)
    password = driver.find_element_by_xpath('//*[@id="root"]/div/form/div/div[2]/div/div/div/input').send_keys("Cp911922@")
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
    
    # WebDriverWait(driver,10).until(lambda x:x.find_element(*input_loc)).send_keys("bbb")
    
    
    

