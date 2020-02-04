
import time
from selenium import webdriver
import requests
import json


def getProxyIp():
    ip_url = 'http://d.jghttp.golangapi.com/getip?num=1&type=2&pro=&city=0&yys=0&port=1&pack=17090&ts=1&ys=0&cs=1&lb=1&sb=0&pb=4&mr=1&regions='
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Mobile Safari/537.36"}
    req = requests.get(ip_url, headers=headers)
    key = req.text
    response = json.loads(key)['data'][0]
    print(response)
    return response


def backworking(countdown, driver):
    if countdown - time.time() <= 15:
        webdriver.Firefox.quit(driver)
        raise ValueError("IP到期")
    else:
        pass


def tiaoye(pageNember, driver, ym):
    page = driver.find_element_by_css_selector('#_view_1545184311000 > div.left_7_3')
    Page = page.text
    K = 0
    while 1:
        try:
            wy = driver.find_element_by_class_name('disabled.pageButton').text
            xyy = "下一页"
            if wy == xyy:
                K = 1
        except:
            pass
        if K == 1:
            last_p = driver.find_element_by_css_selector('#_view_1545184311000 > div.left_7_3').text
            last_P = last_p.split(" ")
            print(last_P[len(last_P) - 3], ym)
            if int(last_P[len(last_P) - 3]) < int(ym):
                raise ValueError("页码过大")
            else:
                pass
        else:
            n = Page.index('下一页')
            if Page.find(str(pageNember), 0, n) >= 0:
                f = driver.find_element_by_link_text(str(pageNember))
                f.click()
                time.sleep(0.5)
                break
            else:
                P = Page.split(" ")
                str1 = P[len(P) - 3]
                f = driver.find_element_by_link_text(str1)
                time.sleep(5)
                f.click()
                time.sleep(5)
                page = driver.find_element_by_css_selector('#_view_1545184311000 > div.left_7_3')
                Page = page.text


def click1(dict0, str1, driver):
    if str1 is None:
        print('全文检索输入有误')
        pass
    else:
        if not len(str1) == 2:
            pass
        else:
            if str1[0] is not None:
                mouseT = driver.find_element_by_css_selector('#qbValue')  # 点击’全文检索‘的输入框
                mouseT.send_keys(str1[0])
            if str1[1] is not None:
                mouseT = driver.find_element_by_css_selector('#qbType')  # 点击‘全文检索’的选择框
                mouseT.click()
                dict1 = {'全文': 1, '首部': 2, '当事人段': 3, '诉讼记录': 4, '事实': 5, '理由': 6,
                         '判决结果': 7, '尾部': 8, '其他': 9}
                xpath = '#qwTypeUl > li:nth-child(%d)' % dict1.get(dict0.get('全文检索')[1])
                mouseT = driver.find_element_by_css_selector(xpath)
                mouseT.click()


def click(counter, xpath0, xpath1, error, driver):
    if counter is None:
        print('%s输入有误' % error)
        pass
    elif counter == 0:
        pass
    else:
        button = driver.find_element_by_css_selector(xpath0)
        driver.execute_script("$(arguments[0]).click()", button)
        time.sleep(1)
        xpath = xpath1 % counter
        button = driver.find_element_by_css_selector(xpath)
        driver.execute_script("$(arguments[0]).click()", button)


def getdata(data):
    f = open('c_10.txt', 'a', encoding='utf-8', errors='ignore')
    f.write(str(data) + '\n')
    f.close()


def caseList(driver):
    caseList = driver.find_elements_by_css_selector(
        '#_view_1545184311000 > div.LM_list > div.list_title.clearfix > h4 > a')
    pstatus["caseList"] = {}
    for x in caseList:
        pstatus["caseList"][x.text] = x.get_attribute('href')
        docId = pstatus["caseList"][x.text][-32:]
        data.update({docId: x.text})


def set15CasePerPg(driver, maxWait=20):
    for x in range(maxWait):
        try:
            e_ = driver.find_element_by_css_selector('#_view_1545184311000 > div.left_7_3 > div > select')
            e_.click()
            e_ = driver.find_element_by_css_selector(
                '#_view_1545184311000 > div.left_7_3 > div > select > option:nth-child(3)')
            e_.click()
            break
        except Exception as e:
            if x == maxWait - 1:
                raise ValueError("15页") from e
            time.sleep(0.5)
    time.sleep(2)


def judge(pageNember, herf_b1, judgepath, driver):
    c1 = driver.find_element_by_css_selector(judgepath)
    herf_c1 = c1.get_attribute('href')
    if herf_c1 == herf_b1:
        print("加载失败")
        time.sleep(1)
        for i in range(1, 20, 1):
            if i == 10:
                a = driver.find_element_by_link_text("下一页")
                a.click()
            if i == 19:
                raise ValueError("网页无法加载")
            try:
                new_c1 = driver.find_element_by_css_selector(judgepath)
                herf_newc1 = new_c1.get_attribute('href')
                if herf_newc1 != herf_b1:
                    print("加载成功")
                    data.clear()
                    caseList(driver)
                    getdata(data)
                    fp = open('页码.txt', 'w', encoding='utf-8')
                    fp.write(str(pageNember + 1))
                    fp.close()
                    break
                else:
                    time.sleep(5)
                    continue
            except Exception:
                pass
    else:
        data.clear()
        caseList(driver)
        getdata(data)
        fp = open('页码.txt', 'w', encoding='utf-8')
        fp.write(str(pageNember + 1))
        fp.close()


def Auto_pageturn(pageNember, driver, judgepath, countdown, maxWait=20):
    while 1:
        k = 1
        backworking(countdown, driver)
        try:
            wy = driver.find_element_by_class_name('disabled.pageButton').text
            xyy = "下一页"
            if wy == xyy:
                k = 2
        except:
            pass
        if k == 2:
            data.clear()
            caseList(driver)
            getdata(data)
            fp = open('页码.txt', 'w')
            fp.write(str(0))
            fp.close()
            break
        for x in range(maxWait):
            try:
                backworking(countdown, driver)
                b1 = driver.find_element_by_css_selector(judgepath)
                herf_b1 = b1.get_attribute('href')
                a = driver.find_element_by_link_text("下一页")
                a.click()
                time.sleep(1)
                judge(pageNember, herf_b1, judgepath, driver)
                pageNember = pageNember + 1
                break
            except Exception as e:
                if x == maxWait - 1:
                    raise ValueError("翻页错误") from e
                time.sleep(0.5)


dict6 = {'': 0, '请选择': 1, '全部': 2, '最高法院': 3, '高级法院': 4, '中级法院': 5, '基层法院': 6}  # 法院层级
dict9 = {'': 0, '请选择': 1, '全部': 2, '判决书': 3, '裁定书': 4, '调解书': 5, '决定书': 6, '通知书': 7, '令': 8, '其他': 9}  # 文书类型
dict7 = {'': 0, '请选择': 1, '管辖案件': 2, '刑事案件': 3, '民事案件': 4, '行政案件': 5, '国家赔偿与司法救助案件': 6, '区际司法协助案件': 7,
         '国际司法协助案件': 8, '司法制裁案件': 9, '非诉保全审查案件': 10, '执行案件': 11, '强制清算与破产案件': 12, '其他案件': 13, '强制清算与破残案件': 12}  # 案件类型
dict11 = {'': 0, '请选择': 1, '指导性案例': 2, '优秀文书': 3}  # 案例等级
dict12 = {'': 0, '请选择': 1, '文书公开': 2, '信息公开': 3}  # 公开类型


def find(dict0, driver):
    for q in dict0:
        if q == '全文检索':
            click1(dict0, dict0[q], driver)
        # if q == '案由':
        #     a = dict0[q]
        #     mouse = driver.find_element_by_id('s16').click()
        #     for y in search.match(a):
        #         print(y,end='')
        #         time.sleep(1)
        #         driver.find_element_by_xpath(y).click()
        if q == '案件名称':
            mouse = driver.find_element_by_css_selector('#s1')
            mouse.send_keys(dict0[q])
        if q == '案号':
            mouse = driver.find_element_by_css_selector('#s7')
            mouse.send_keys(dict0[q])
        if q == '法院名称':
            mouse = driver.find_element_by_css_selector('#s2')
            for i in dict0[q]:
                mouse.send_keys(i)
        if q == '法院层级':
            click(dict6.get(dict0[q]), '#s4', '#gjjs_fycj > li:nth-child(%d)', q, driver)
        if q == '案件类型':
            click(dict7.get(dict0[q]), '#s8', '#gjjs_ajlx > li:nth-child(%d)', q, driver)
        if q == '文书类型':
            click(dict9.get(dict0[q]), '#s6', '#gjjs_wslx > li:nth-child(%d)', q, driver)
        if q == '裁判日期':
            if len(dict0[q]) != 2:
                print('裁判日期输入有误!')

            else:
                mouse = driver.find_element_by_id('cprqStart')
                for i in dict0[q][0]:
                    mouse.send_keys(i)
                mouse = driver.find_element_by_id('cprqEnd')
                mouse.send_keys(dict0[q][1])
                mouse = driver.find_element_by_css_selector(
                    '#_view_1545034775000 > div > div.advencedWrapper')  # 输入完之后日历遮挡页面，需要点击空白消掉
                mouse.click()
        if q == '案例等级':
            click(dict11.get(dict0[q]), '#s44', '#gjjs_aldj > li:nth-child(%d)', q, driver)
        if q == '公开类型':
            click(dict12.get(dict0[q]), '#s43', '#gjjs_gklx > li:nth-child(%d)', q, driver)
        if q == '审判人员':
            mouse = driver.find_element_by_css_selector('#s18')
            mouse.send_keys(dict0[q])
        if q == '当事人':
            mouse = driver.find_element_by_css_selector('#s17')
            mouse.send_keys(dict0[q])
        if q == '律所':
            mouse = driver.find_element_by_css_selector('#s20')
            mouse.send_keys(dict0[q])
        if q == '律师':
            mouse = driver.find_element_by_css_selector('#s19')
            mouse.send_keys(dict0[q])
        if q == '法律依据':
            mouse = driver.find_element_by_css_selector('#flyj')
            mouse.send_keys(dict0[q])
    time.sleep(2)
    go = driver.find_element_by_css_selector('#searchBtn')
    go.click()


def caseNember(driver):
    for i in range(1, 7, 1):
        if i == 6:
            raise ValueError("文件数量")
        try:
            if i == 1:
                pass
            else:
                time.sleep(1)
            number = driver.find_element_by_css_selector(
                '#_view_1545184311000 > div.LM_con.clearfix > div.fr.con_right > span')
            number1 = number.text
            number = int(number1)
            print("本次检索数量：", number)
            run_log("本次检索数量： %s" % number)
            if number > 100000:
                continue
            elif number < 0 or number == 0:
                return 1
            elif number <= 15:
                return 2
            else:
                break
        except Exception:
            pass


def getProfirle():
    profile_ = webdriver.FirefoxProfile()
    profile_.set_preference('network.proxy.type', 1)
    proxyIp = proIP
    proIp = str(proxyIp['ip'])  # IP
    proPort = int(proxyIp['port'])  # 端口
    time_str = proxyIp['expire_time']  # 字符类型的时间
    timeArray = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")  # 转为时间数组
    proTimeStamp = int(time.mktime(timeArray))  # 转为时间戳
    # print("IP到期还有%ss" % (proTimeStamp - time.time()))
    # print(proTimeStamp)  # 时间戳
    # proTimeStamp = proxyIp[0]['expire']  # 有效时间的时间戳  # float
    # countdown = proTimeStamp - time.time()
    # profile_.set_preference('permissions.default.image', 2)
    # profile_.set_preference('javascript.enabled', 'false')
    # profile_.set_preference('permissions.default.stylesheet', 2)
    profile_.set_preference('network.proxy.http', proIp)
    profile_.set_preference('network.proxy.http_port', proPort)  # int
    profile_.set_preference("network.proxy.share_proxy_settings", True)
    return profile_, proTimeStamp


def working():
    global driver
    f = open(r"10.txt", "r", encoding='gbk')
    s = f.read()
    s = s.split()
    ff = open(r"状态.txt", "r", encoding='utf-8-sig')  # 读取状态文本
    aa = ff.read()
    aa = s.index(aa)
    for i in range(len(s) - aa):
        print(eval(s[i + aa]))
        run_log(eval(s[i + aa]))
        fff = open(r"状态.txt", "w", encoding='utf-8')
        fff.write(s[i + aa])
        fff.close()
        dict0 = eval(s[i + aa])
        profile_, countdown = getProfirle()
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(executable_path="driver\geckodriver", firefox_profile=profile_)
        url = "http://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html"
        driver.get(url)
        maxWait = 50
        for x in range(maxWait):
            try:
                if ((x + 1) % 10) == 0:
                    driver.refresh()
                a = driver.find_element_by_css_selector(
                    '#_view_1545034775000 > div > div.search-wrapper.clearfix > div.advenced-search')
                a.click()
                find(dict0, driver)
                break
            except Exception as e:
                if x == maxWait - 1:
                    raise ValueError("高级检索") from e
                time.sleep(0.5)
        judgePath = "#_view_1545184311000 > div:nth-child(3) > div.list_title.clearfix > h4 > a"
        k1 = caseNember(driver)
        time.sleep(1)
        if k1 == 1:
            webdriver.Firefox.quit(driver)
            continue
        if k1 == 2:
            fp = open('页码.txt', 'w')
            fp.write(str(1))
            fp.close()
            set15CasePerPg(driver, maxWait=20)
            caseList(driver)
            getdata(data)
            fp = open('页码.txt', 'w')
            fp.write(str(0))
            fp.close()
            webdriver.Firefox.quit(driver)
            continue
        g = open(r"页码.txt", "r", encoding='utf-8-sig')
        ym = g.read()
        if ym != '0':
            pageNember = int(ym)
            set15CasePerPg(driver, maxWait=20)
            backworking(countdown, driver)
            tiaoye(pageNember, driver, ym)
            caseList(driver)
            getdata(data)
            backworking(countdown, driver)
            Auto_pageturn(pageNember, driver, judgePath, countdown, maxWait=20)
            webdriver.Firefox.quit(driver)
            continue
        else:
            pass
        set15CasePerPg(driver, maxWait=20)
        fp = open('页码.txt', 'w')
        fp.write(str(1))
        fp.close()
        caseList(driver)
        getdata(data)
        pageNember = 1
        Auto_pageturn(pageNember, driver, judgePath, countdown, maxWait=20)
        webdriver.Firefox.quit(driver)


def run_log(log):
    run_file = open(r'第二十参数运行日志.txt', 'a', encoding='utf-8')
    run_file.write(str(log) + '\n')


def send_up():
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr

    my_sender = '1274605040@qq.com'  # 发件人邮箱账号
    my_pass = 'vouyqhmiddfxfjga'  # 发件人邮箱密码
    my_user = '1274605040@qq.com'  # 收件人邮箱账号，我这边发送给自己

    def mail(subject):
        ret = True
        try:
            msg = MIMEText('鸭鸭鸭,我好像崩溃了(ง ˙o˙)ว', 'plain', 'utf-8')
            msg['From'] = formataddr(("光", my_sender))  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(("FK", my_user))  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = "爬虫出错" + str(subject)  # 邮件的主题，也可以说是标题

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
            server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False
        return ret

    import socket
    my_ip = socket.gethostbyname(socket.getfqdn(socket.gethostname()))
    print(my_ip)
    ret = mail(my_ip)
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")


def getProfirle_main():
    proxyIp = getProxyIp()  # 获取代理IP
    return proxyIp


if __name__ == '__main__':
    global driver

    ip_flag = 30  # 代码运行一共获取的IP数量
    while ip_flag:
        # print("ip_flag: %s" % ip_flag)
        ip_flag -= 1  # 获取IP数量减一
        ip_judge = 5  # 判断IP是否可用
        proIP = getProfirle_main()
        i = 500
        while i:
            i -= 1
            if i == 10:
                send_up()
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            run_log(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            pstatus = {}
            data = {}
            try:
                # profile_, countdown = getProfirle()
                working()
            except Exception as e:
                print('错误原因', e)
                if "由于目标计算机积极拒绝，无法连接" in str(e):
                    i += 1

                elif "15页" in str(e):
                    i += 1
                    print(i)
                elif str(e) == "页码过大":
                    i += 1
                    fp = open('页码.txt', 'w')
                    fp.write(str(0))
                    fp.close()
                elif str(e) == "高级检索":
                    i += 1
                elif str(e) == "IP到期":
                    print("重新获取IP")
                    break
                elif "Reached error page: about:neterror?" in str(e):
                    ip_judge -= 1
                    if not ip_judge:
                        ip_flag += 1
                        print("IP不可用")
                        break
                else:
                    pass
                try:
                    webdriver.Firefox.quit(driver)
                except Exception:
                    pass
