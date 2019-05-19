import os
import sys
#项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#添加系统环境变量
sys.path.append(BASE_DIR)

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from wechat.util import Util



chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--headless')
# online
# driver = webdriver.Chrome(chrome_options=chrome_options)
# local
driver = webdriver.Chrome(executable_path='../chromedriver', chrome_options=chrome_options)
driver.fullscreen_window()

url = "https://mp.weixin.qq.com/"

driver.get(url)

cookie_str = "pgv_pvi=3933481984; RK=gO+G5oSuag; ua_id=cO8KF9lwAeqsWbhzAAAAAKmwS9Frqqz43N55MOY-9dQ=; ts_uid=9614619520; tvfe_boss_uuid=a603f0c88ca6e847; pgv_pvid=3428510079; ptcz=637b0eddfcbb5504be18dd73a884b5b31e6991a7c12d8dc790062cec80450816; eas_sid=F1q5y2U733E4E6r7Z6f8q7d9w6; mm_lang=zh_CN; _ga=GA1.2.151957035.1536739292; o_cookie=601279271; pac_uid=1_601279271; __root_domain_v=.weixin.qq.com; _qddaz=QD.nf2ikh.c5fa3.jpibntai; pgv_si=s8667681792; cert=c_RJDbM0RHrf8mvlHSePup2Ln3rW7s3X; wxuin=55345575840186; uin=o0601279271; skey=@rsWU460ex; ptisp=ctc; pgv_info=ssid=s5296057300; rv2=80414B0A980CA42282B464C7249F802EE58E89E10797D8A781; property20=40F35AF00CAA3FDFADEE6BBFA66549F5806C0481F31E20644E45652AB8E5A4328B57B672B22B8C30; rewardsn=; wxtokenkey=777; uuid=932c9d90ba52afa80695e261636f323f; ticket=7b673da4de14027ceeef5ee1b28cf0ad0bdc0cdc; ticket_id=gh_63ec5d3d8972; noticeLoginFlag=1; data_bizuin=3013547929; bizuin=3006549343; data_ticket=CQ2Gzus4iy5sZ590GsOXS0DI4/lsVJaQYDzFXx1LJsTWA1jUalbnuGswE9EzQVJ7; slave_sid=emp5SXFtRzBndnZLanNOMmtCZVV0eDJVZ2JFNjNkOWQwZ0U0WVphVGE2Z1hPS0VwSElZZHdZVmhCVDNVRVN1b0VTM3FXcXoyMkhHeXFXX3B2VEdwN2dTZXZIemVoWUhPYzVJSkNlZU1kcWp5Wk9TSjFCV0NwUE5mS25CNFFkT0FlSHVnQ3c2VVhuTG5ZOHBu; slave_user=gh_63ec5d3d8972; xid=6afbb83b3cbf48b113665d49d55474cf; openid2ticket_omRefs7iCjMLMX2EIuYIh4r3AmnQ=iDF4ht8QW03VXEdB2lclGNkIV1uSf5Sl4apShUXWaig="

# 登录微信公众平台后，打开浏览器开发工具，在请求的header中可以找到cookie
cookie_str = ""
#从浏览器获取到的cookie是字符串的，需要处理成一个个dict {"name":"", "value":""}
cookie_dict_list = Util().handle_cookie(cookie_str)

for cookie_dict in cookie_dict_list:
    driver.add_cookie(cookie_dict)

# 要想登录页面需要先添加cookie
# 点击新建素材页面后的网页地址
url = "https://mp.weixin.qq.com/cgi-bin/appmsg?开头"

#url = "https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit_v2&action=edit&isNew=1&type=10&token=898781527&lang=zh_CN"
driver.get(url)

# 这里是模拟点击超链接的地方
driver.find_element_by_id("edui24_body").click()

driver.find_element_by_xpath('//*[@id="myform"]/div[3]/div[1]/div/label[2]/i').click()
driver.find_element_by_class_name('js_acc_search_input').send_keys("youthmba")
driver.find_element_by_class_name('js_acc_search_btn').click()


wait = WebDriverWait(driver, 5)

element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search_biz_result_wrap')))

element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search_biz_result')))
element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'js_acc_item')))
element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search_biz_info')))
driver.find_element_by_class_name("search_biz_result").click()
element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'js_article_content')))
element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search_article_result')))
element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'my_link_list')))
link_elements = driver.find_element_by_class_name(" my_link_list").find_elements_by_tag_name('a')
date_elements = driver.find_element_by_class_name(" my_link_list").find_elements_by_class_name("date")


# 取当日的文章内容
today = datetime.now().strftime("%Y-%m-%d")
today_date = []
# 日期内容是和文章链接个数相同的，找出多少个今天的日期，就如多少个链接即可。
for one in date_elements:
    if today == one.get_attribute("textContent"):
        today_date.append(one)

for one in link_elements[0:len(today_date)]:
    print(one.get_attribute("href"))
    print(one.get_attribute("text"))
driver.quit()
