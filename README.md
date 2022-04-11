# caipanwenshu_spider

### 爬取流程

* 爬取文书每篇文书的docid

* 依据docid爬取正文，概要和法律依据

### 感谢

* 感谢[李唐](https://github.com/itangk)提供的部分代码

### 代码

* [获取每篇文书的docid](https://github.com/Day-Bright/caipanwenshu_spider/blob/master/wenshu/getDocid.py)

* [获取文书的正文，概要和法律依据](https://github.com/Day-Bright/caipanwenshu_spider/blob/master/wenshu/GetWenshu.py)

* [将左侧地域列表加入](https://github.com/Day-Bright/caipanwenshu_spider/blob/master/wenshu/area.py)

* [解析爬下来的文件](https://github.com/Day-Bright/caipanwenshu_spider/blob/master/wenshu/Analyticak_wenshu.py)

### 注意事项

* 想要爬的数据多`，参数得做的全面

### 更新

* 文书网登录

  * 2021/10/6新增[裁判文书网登录](https://github.com/Day-Bright/caipanwenshu_spider/blob/master/cpws_login/cpws_login.py)，JS逆向登录加密

  * 2022/4/11新增[裁判文书网登录](https://github.com/Day-Bright/caipanwenshu_spider/blob/master/cpws_login/LoginByUC.py)，使用undetected_chromedriver绕过文书网对selenium的反爬措施











