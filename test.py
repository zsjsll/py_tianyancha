import codecs
import time
import urllib.request as tran

# from bs4 import BeautifulSoup
from lxml import etree

from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap["phantomjs.page.settings.userAgent"] = (
#     "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0")
# driver = webdriver.PhantomJS(
#     executable_path='D:/phantomjs/bin/phantomjs.exe',
#     desired_capabilities=dcap)

# 浏览器不加载图片
chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2} 
chromeOptions.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(executable_path='D:/chromedriver/chromedriver.exe',chrome_options=chromeOptions)

# driver.get('http://www.tianyancha.com/company/2310290454')
# time.sleep(5)
# # 获取网页内容
# content = driver.page_source.encode('utf-8')
# driver.close()
# print(content.decode('utf-8'))
dictcom = {}
company = [
    '光达',
    '滇中恒达',
    '山东新华制药股份有限公司',
]
for x in company:
    # print(tran.quote(x))
    driver.get('http://www.tianyancha.com/search?key=%s&checkFrom=searchBox' %
               (tran.quote(x)))
    is_disappeared = WebDriverWait(driver, 8, 0.5, ignored_exceptions=TimeoutException)
    WebDriverWait.until(lambda x: x.find_element_by_id("id").is_displayed())
    time.sleep(5)
    conten = driver.page_source
    # driver.close()
    # print(content)
    html = etree.HTML(conten)
    # code = etree.tostring(html, pretty_print=True)
    # print(code)
    selector = html.xpath(
        '//*[@id="ng-view"]/div[2]/div/div/div[1]/div[3]/div/div[2]/div[1]/div[1]/a/span'
    )
    inno = selector[0].xpath('string()')
    # print(inno)
    selector = html.xpath(
        '//*[@id="ng-view"]/div[2]/div/div/div[1]/div[3]/div/div[2]/div[1]/div[1]/a/@href'
    )
    # print(selector)
    companyUrl = selector[0]
    # print(companyUrl)

    dictcom[inno] = companyUrl
    # print(dictcom)
f = codecs.open('dictcom.txt', 'w', 'utf-8')
f.write(str(dictcom))
f.close

for (k, v) in dictcom.items():

    #print(k, v)
    driver.get(v)
    time.sleep(5)
    content = driver.page_source

    # print(content)
    html = etree.HTML(content)

    print("'-------基本信息-------'")
    selector = html.xpath(
        '//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div[1]/div[2]/div/span/text()'
    )
    companyName = selector[0]
    print('公司名字：', companyName)

    selector = html.xpath(
        '//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/span[2]/text()'
    )
    companyphone = selector[0]
    print('电话：', companyphone)

    selector = html.xpath(
        '//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div[1]/div[2]/div/div[2]/div[2]/span[2]/text()'
    )
    companymail = selector[0]
    print('邮箱：', companymail)

    selector = html.xpath(
        '//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div[1]/div[2]/div/div[3]/div[1]/span[2]/text()'
    )
    company3w = selector[0]
    print('网址：', company3w)

    selector = html.xpath(
        '//*[@id="ng-view"]/div[2]/div/div/div/div[1]/div[1]/div[2]/div/div[3]/div[2]/span[2]/text()'
    )
    companyaddr = selector[0]
    print('地址：', companyaddr)

    print("--------------\n")

    print('-------详细信息-------')

    selector = html.xpath(
        '//*[@class="baseInfo_model2017"]/table/tbody/tr/td[1]/a/text()')

    legal = selector[0]
    print('法人代表：', legal)

    selector = html.xpath(
        '//*[@class="baseInfo_model2017"]/table/tbody/tr/td[2]/div/text()')
    money = selector[0]
    print('注册资本：', money)

    selector = html.xpath(
        '//*[@class="baseInfo_model2017"]/table/tbody/tr/td[3]/div/text()')
    createTime = selector[0]
    print('注册时间：', createTime)

    selector = html.xpath(
        '//*[@class="baseInfo_model2017"]/table/tbody/tr/td[4]/div/text()')
    nowstate = selector[0]
    print('经营状态：', nowstate)

    print("--------------\n")

    selector = html.xpath(
        '//*[@class="row b-c-white company-content base2017"]/table/tbody/tr[2]/td[2]/div/span/text()'
    )
    comtype = selector[0]
    print('企业类型：', comtype)

    selector = html.xpath(
        '//*[@class="row b-c-white company-content base2017"]/table/tbody/tr[3]/td[1]/div/span/text()'
    )
    tp = selector[0]
    print('行业：', tp)

    selector = html.xpath(
        '//*[@class="row b-c-white company-content base2017"]/table/tbody/tr[4]/td[2]/div/span/text()'
    )
    register = selector[0]
    print('登记机关：', register)

    selector = html.xpath(
        '//*[@class="row b-c-white company-content base2017"]/table/tbody/tr[5]/td[1]/div/span/text()'
    )
    registeraddr = selector[0]
    print('注册地址：', registeraddr)

    selector = html.xpath(
        '//*[@class="row b-c-white company-content base2017"]/table/tbody/tr[6]/td/div/span/span/text()'
    )
    comrange = selector[0]
    print('经营范围：', comrange)

    prto = {}
    prto[''] = '-------基本信息-------'
    prto['公司名字'] = companyName
    prto['电话'] = companyphone
    prto['邮箱'] = companymail
    prto['网址'] = company3w
    prto['地址'] = companyaddr
    prto[' '] = '--------------'
    prto['  '] = '-------详细信息-------'
    prto['法人代表'] = legal
    prto['注册资本'] = money
    prto['注册时间'] = createTime
    prto['经营状态'] = nowstate
    prto['企业类型'] = comtype
    prto['行业'] = tp
    prto['登记机关'] = register
    prto['注册地址'] = registeraddr
    prto['经营范围'] = comrange
    prto['   '] = '--------------'

    comtxt=companyName+".txt"
    save=codecs.open(comtxt,'a','utf-8')
    for (k,v)in prto.items():
        line=k,':',v+'\n'
        save.writelines(line)
    save.close


driver.close()
