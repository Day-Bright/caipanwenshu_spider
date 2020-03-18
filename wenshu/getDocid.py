import time
from selenium import webdriver
from src import search


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
    f = open('guosi.txt', 'a', encoding='utf-8', errors='ignore')
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


def judge(pageNember, herf_b1, judgePath, driver):
    c1 = driver.find_element_by_css_selector(judgePath)
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
                new_c1 = driver.find_element_by_css_selector(judgePath)
                herf_newc1 = new_c1.get_attribute('href')
                if herf_newc1 != herf_b1:
                    print("加载成功")
                    caseList(driver)
                    getdata(data)
                    data.clear()
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
        caseList(driver)
        getdata(data)
        data.clear()
        fp = open('页码.txt', 'w', encoding='utf-8')
        fp.write(str(pageNember + 1))
        fp.close()


def Auto_pageturn(pageNember, driver, judgePath, maxWait=20):
    while 1:
        k = 1
        try:
            wy = driver.find_element_by_class_name('disabled.pageButton').text
            xyy = "下一页"
            if wy == xyy:
                k = 2
        except:
            pass
        if k == 2:
            caseList(driver)
            getdata(data)
            data.clear()
            fp = open('页码.txt', 'w')
            fp.write(str(0))
            fp.close()
            break
        for x in range(maxWait):
            try:
                b1 = driver.find_element_by_css_selector(judgePath)
                herf_b1 = b1.get_attribute('href')
                a = driver.find_element_by_link_text("下一页")
                a.click()
                time.sleep(1)
                judge(pageNember, herf_b1, judgePath, driver)
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
        if q == '案由':
            a = dict0[q]
            mouse = driver.find_element_by_id('s16').click()
            for y in search.match(a):
                # print(y,end='')
                time.sleep(1)
                driver.find_element_by_xpath(y).click()
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
    return profile_


def working():
    global driver
    f = open(r"参数.txt", "r", encoding='utf-8')
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
        profile_ = getProfirle()
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
            data.clear()
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
            tiaoye(pageNember, driver, ym)
            caseList(driver)
            getdata(data)
            data.clear()
            Auto_pageturn(pageNember, driver, judgePath, maxWait=20)
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
        data.clear()
        pageNember = 1
        Auto_pageturn(pageNember, driver, judgePath, maxWait=20)
        webdriver.Firefox.quit(driver)


def run_log(log):
    run_file = open(r'第二十参数运行日志.txt', 'a', encoding='utf-8')
    run_file.write(str(log) + '\n')




if __name__ == '__main__':
    global driver
    i = 500
    while i:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        pstatus = {}
        data = {}
        try:
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
            else:
                pass
            try:
                webdriver.Firefox.quit(driver)
            except Exception:
                pass