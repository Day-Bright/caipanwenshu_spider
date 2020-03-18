import multiprocessing
import os
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from multiprocessing import Pool
import requests
import json


def getProxyIp():
    response = requests.get(
        r'http://112.17.250.13:88/open?user_name=ly_2814623_ce92&timestamp=1554706833&md5=94a19c9473b12e492966a2daa281c4c6&pattern=josn&number=1&special=0').json()
    if response['code'] != 100:
        print("IP问题")
    print(response)
    res = {'ip': response['domain'], 'port': response['port'][0], 'expire': response['left_time']}
    return res


def getProfirle(ip_message):
    if ip_message is None:
        profile = webdriver.FirefoxOptions()
        # profile.set_preference('browser.cache.disk.parent_directory', r'D:\Temp Files')
    else:
        profile = webdriver.FirefoxOptions()
        # profile.set_preference('browser.cache.disk.parent_directory', r'D:\Temp Files')
        # profile.set_preference('browser.cache.offline.parent_directory', r'D:\Temp Files')
        profile.set_preference('network.proxy.type', 1)
        proxyIp = ip_message
        proIp = str(proxyIp['ip'])  # IP
        proPort = int(proxyIp['port'])  # 端口
        proTimeStamp = proxyIp['expire']  # 有效时间的时间戳  # float
        profile.set_preference('network.proxy.http', proIp)
        profile.set_preference('network.proxy.http_port', proPort)  # int
        profile.set_preference("network.proxy.share_proxy_settings", True)
    return profile


def get_text(docid_, driver_, file_number):
    PDF = ''
    basic_inf = ''
    legal_basis = ''
    url = str('http://wenshu.court.gov.cn/website/wenshu/181107ANFZ0BXSK4/index.html?docId=') + str(docid_)
    driver.get(url)
    maxWait = 100
    for x in range(maxWait):
        if (x + 1) % 2 == 0:
            driver.refresh()
        try:
            WebDriverWait(driver, 3).until(lambda x: x.find_element_by_css_selector('.PDF_box'))
            gaiyao = driver.find_element_by_css_selector(
                '#_view_1541573889000 > div:nth-child(1) > div.right_fixed > div.right_btn')
            gaiyao.click()
            break
        except Exception as e:
            if x == maxWait - 1:
                raise ValueError("概要") from e
            time.sleep(0.5)
    for x in range(maxWait):
        try:
            PDF = driver.find_element_by_css_selector('.PDF_box')
            basic_inf = driver.find_element_by_css_selector(
                '#_view_1541573889000 > div:nth-child(1) > div.right_fixed > div.gaiyao_box > div.gaiyao_center > ul > li:nth-child(1)')
            legal_basis = driver.find_element_by_css_selector(
                '#_view_1541573889000 > div:nth-child(1) > div.right_fixed > div.gaiyao_box > div.gaiyao_center > ul > li:nth-child(2)')
            break
        except Exception:
            if x == maxWait - 1:
                webdriver.Firefox.quit(driver_)
                raise ValueError("无法获取文件")
            time.sleep(0.5)
    text = '<docid>' + '\n' + json.dumps(docid_) + '\n' + '<docid>' + '\n' + \
           '<major_text>' + '\n' + json.dumps(PDF.text) + '\n' + '<major_text>' + '\n' + \
           '<basic_inf>' + '\n' + json.dumps(basic_inf.text) + '\n' + '<basic_inf>' + '\n' + \
           '<legal_basis>' + '\n' + json.dumps(legal_basis.text) + '\n' + '<legal_basis>''\n'
    lock.acquire(block=False)
    file = open(r'E:\wenshu\wenshu%s.txt' % file_number, 'a', encoding='utf-8')
    file.write(str(text) + '\n')
    file.close()
    file_ = open(r'E:\wenshu\状态docid_%s.txt' % file_number, 'a', encoding='utf-8')
    file_.write(docid_ + '\n')
    file_.close()
    # lock.release()


def body(ip_message, file_number):
    global driver
    try:
        profile = getProfirle(ip_message)
        driver = webdriver.Firefox(options=profile)
        driver.set_page_load_timeout(40)
        driver.set_script_timeout(40)  # 这两种设置都进行才有效
        while queue.qsize():
            docid = queue.get()
            get_text(docid, driver, file_number)
    except Exception as e:
        webdriver.Firefox.quit(driver)
        return e
    else:
        webdriver.Firefox.quit(driver)


def init(l_, q_):
    global lock
    global queue
    lock = l_
    queue = q_


def pool(file_number):
    # 获取CPU核数
    core_number = multiprocessing.cpu_count()
    f = open(r'E:\wenshu\docid.txt', 'r', encoding='utf-8')
    a = f.read()
    a = set(a.split())
    ff = open(r'E:\wenshu\状态docid_%s.txt' % file_number, 'r', encoding='utf-8')
    zhuangt = set(ff.read().split())
    a = a.difference(zhuangt)
    a = list(a)
    # 初始化进程池 同时创建全局进程锁和队列
    lock = multiprocessing.Lock()
    queue = multiprocessing.Queue()
    for q in a[:]:
        queue.put(q)
    while queue.qsize():  # 当队列里有元素的时候
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print(queue.qsize())
        # 获取代理IP信息  response_IP  节约上面初始化参数的那么一秒半秒的时间
        response_IP = getProxyIp()
        p = Pool(core_number, initializer=init, initargs=(lock, queue,))  # 初始化进程池
        response = []
        for number in range(core_number):  # core_number CPU核数,开启CPU核数的进程,每个核负责一个进程
            res = p.apply_async(body, args=(response_IP, file_number,))
            response.append(res)
        p.close()
        p.join()


def main(file_number):
    pool(file_number)


if __name__ == '__main__':
    while True:
        try:
            file_number = input("请输入本机要爬的参数序号")
            if not os.path.exists(r'E:\wenshu\状态docid_%s.txt' % file_number):  # 文件存在则返回True,不存在返回False
                fd = open(r'E:\wenshu\状态docid_%s.txt' % file_number, 'a', encoding='utf-8')
                fd.close()
            else:
                pass
            main(file_number)
        except Exception as e:
            print("Boom error", e)
            continue