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

# 登录微信公众平台后，打开浏览器开发工具，在请求的header中可以找到cookie
cookie_str = ""
#从浏览器获取到的cookie是字符串的，需要处理成一个个dict {"name":"", "value":""}
cookie_dict_list = Util().handle_cookie(cookie_str)

for cookie_dict in cookie_dict_list:
    driver.add_cookie(cookie_dict)

# 要想登录页面需要先添加cookie
# 点击新建素材页面后的网页地址
url = "https://mp.weixin.qq.com/cgi-bin/appmsg?开头"

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
