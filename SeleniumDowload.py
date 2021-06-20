#利用xpath的規則點擊按鈕，selenium會將這些檔案下載到目錄"下載"底下，然後再將這些excel檔自行拉去當下資料夾中的'全國電影票房'
#記得要將chromedriver拉到與此檔案目錄底下
#version 1 2021/3/13
import re
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
path = './全國電影票房'
if not os.path.isdir(path):
    os.mkdir(path)          #創建放excel檔的資料夾

driver = webdriver.Chrome()
driver.get('https://www.tfi.org.tw/BoxOfficeBulletin/weekly')
time.sleep(3)
for i in range(191):

    e = driver.find_element_by_xpath('//*[@id="main-content"]/section[2]/div/section[2]/div/div/div/table/tbody/tr['+ str(i + 1) + ']/td[5]/a')
    e.click()
    