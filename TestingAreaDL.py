##############################################################################
# Testing File with just one chanel to download
import time
import requests
import re
import os
import errno
import shutil
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from operator import is_not
from functools import partial
import datetime
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

now = datetime.datetime.now()
url = 'https://www.jodel.city/4321'
#url = 'https://www.winfuture.de'

#browser = webdriver.Chrome()

#browser.get(url)
#browser.get(url)

#elem = browser.find_element_by_id('contentArea')
#contentList = elem.find_elements_by_tag_name('li')

#out =browser.execute_script('$.ajax({data: {ajax: 1,no: 1,to: 600}, cache: false,});')

#print(out)

tmp = requests.get('https://www.jodel.city/6789?ajax=1&no=200&to=300')
tmp = requests.get('https://www.jodel.city/6789?ajax=1&no=200&to=300')
print(tmp.content)

# if(len(contentList) > 30):
#     info = browser.find_element_by_xpath('//*[@id="contentArea"]/li[30]')
#     browser.execute_script("arguments[0].scrollIntoView();", info)
# time.sleep(1)
# if(len(contentList) > 45):
#     info = browser.find_element_by_xpath('//*[@id="contentArea"]/li[45]')
#     browser.execute_script("arguments[0].scrollIntoView();", info)
# time.sleep(1)
# if(len(contentList) > 60):
#     info = browser.find_element_by_xpath('//*[@id="contentArea"]/li[60]')
#     browser.execute_script("arguments[0].scrollIntoView();", info)

# elem = browser.find_element_by_id('contentArea')
# contentList = elem.find_elements_by_tag_name('li')

# print("----------------------------")
# print(len(contentList))
# for i in contentList:
#     print(i.text)
photostr = []

# while(len(contentList) > 65):
#     elem = browser.find_element_by_id('contentArea')
#     contentList = elem.find_elements_by_tag_name('li')
#     if(len(contentList) > 30):
#         info = browser.find_element_by_xpath('//*[@id="contentArea"]/li[30]')
#         browser.execute_script("arguments[0].scrollIntoView();", info)
#     if(len(contentList) > 45):
#         info = browser.find_element_by_xpath('//*[@id="contentArea"]/li[45]')
#         browser.execute_script("arguments[0].scrollIntoView();", info)
#     if(len(contentList) > 60):
#         info = browser.find_element_by_xpath('//*[@id="contentArea"]/li[60]')
#         browser.execute_script("arguments[0].scrollIntoView();", info)
#     time.sleep(1)

#     for row in contentList:
#         #print(row.text)
#         photoRow = browser.find_elements_by_xpath(".//*[@class='ic']")
#         for ph in photoRow:
#             tmp = ph.get_attribute('data-navigation')
#             if(tmp.__contains__('vid')):
#                 #Videos
#                 tmp = 'https://i.jodel.me/' + tmp[4:] + '.mp4'
#             else:
#                 #Pictures
#                 tmp = 'https://g.jodel.me/' + tmp[6:] + 't.jpg'
#             photostr.append(tmp)
#     print("----------------------------")
#     if(len(contentList) > 65):
#         info = browser.find_element_by_xpath('//*[@id="contentArea"]/li[65]')
#         browser.execute_script("arguments[0].scrollIntoView();", info)

# photostr = list(dict.fromkeys(photostr))
# for i in photostr:
#     print(i)

#browser.quit()


#time.sleep(3)

#elem = browser.find_element_by_id('contentArea')
#contentList = elem.find_elements_by_tag_name("li")

#selects = Select(browser.find_element_by_xpath('//*[@id="contentArea"]/li[1]'))
#selects.deselect_all()

# info = browser.find_element_by_xpath('//*[@id="contentArea"]/li[10]')
# browser.execute_script("arguments[0].scrollIntoView();", info)
# time.sleep(1)
# for i in contentList:
#     print(i.text)
# info = browser.find_element_by_xpath('//*[@id="contentArea"]/li[20]')
# browser.execute_script("arguments[0].scrollIntoView();", info)
# time.sleep(1)
# info = browser.find_element_by_xpath('//*[@id="contentArea"]/li[40]')
# browser.execute_script("arguments[0].scrollIntoView();", info)
# time.sleep(1)
# info = browser.find_element_by_xpath('//*[@id="contentArea"]/li[66]')
# browser.execute_script("arguments[0].scrollIntoView();", info)
# time.sleep(1)

# print('--------------------------------------------------------')
# info = browser.find_element_by_xpath('//*[@id="contentArea"]/li[]')
# browser.execute_script("arguments[0].scrollIntoView();", info)
# time.sleep(1)
# elem = browser.find_element_by_id('contentArea')
# contentList = elem.find_elements_by_tag_name("li")
# for i in contentList:
#     print(i.text)


#browser.execute_script("window.scrollTo(0, 1080);")
#browser.execute_script("window.scrollTo(0, 1080);")
#browser.execute_script("window.scrollTo(0, 1080);")


#browser.sendKeys(Keys.DOWN)
#info.send_keys(Keys.DOWN)
#info.send_keys(Keys.DOWN)
#dropdown = browser.find_elements_by_class_name('padded-list')
#dropdowntList = dropdown.find_elements_by_tag_name("li")



#htmls = browser.page_source
#print(htmls)

#browser.quit()



# chanels = []
# for t in dropdown:
#     if(t.get_attribute("data-value") != None):
#         chanels.append(t.get_attribute("data-value"))

# for i in chanels:
#     print(i)

# photostr = []
# chanalTitel = browser.title
# print(browser.title)

# for row in contentList:
#     photoRow = row.find_elements_by_xpath(".//*[@class='ic']")
#     for ph in photoRow:
#         tmp = ph.get_attribute("data-navigation")
#         photostr.append(tmp[6:])
# browser.quit()

# #Get the pics
# for x in photostr:
#     picure = x + 't.jpg'
#     tmp = "https://g.jodel.me/" + picure
#     path = str(datetime.datetime.today()).split()[0] + "/" + chanalTitel + "/" + picure
#     print(path)
#     if not os.path.exists(os.path.dirname(path)):
#         try:
#             os.makedirs(os.path.dirname(path))
#         except OSError as exc: # Guard against race condition
#             if exc.errno != errno.EEXIST:
#                 raise
#     response = requests.get(tmp, stream=True)
#     with open( path, 'wb') as out_file:
#         shutil.copyfileobj(response.raw, out_file)
#     del response
#     print(x)

#str(datetime.datetime.today()).split()[0] +

#ua = UserAgent()
#headers = {'User-Agent': ua.Firefox}
#pic = browser.find_element_by_css_selector('body.web:nth-child(2) #home.app-page.app-active:nth-child(8) div.content div.tab-content:nth-child(1) ul.list #li.img:nth-child(21) div.ic div:nth-child(1) > div.entry')
#print(pic.get_property("style")['background-image'])
#res = requests.get(url, headers=headers ,allow_redirects=False)