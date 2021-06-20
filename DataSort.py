#file erro!!! 全國電影票房2020年0921-0927統計資訊(網站那邊連結給錯)
#file erro!!! 全國電影票房2020年0803-0809統計資訊(網站那邊連結給錯)
#file erro!!! 全國票房2019年0722-0728統計資訊(此檔案有問題!!!已修正(上方表格名稱格式不同))(已自行在此檔案裡做修改成正常格式)
#version 1 2021/6/13
import pandas as pd
import re
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import os

path = './2021到2017資料'
if not os.path.isdir(path):
    os.mkdir(path)          #創建放excel檔的資料夾

datayear = ['year2021', 'year2020', 'year2019', 'year2018', 'year2017']
for i in range(len(datayear)):
    datayear[i] = {"國別地區":[],
            "中文片名":[],
            "上映日期":[],
            "申請人":[],
            "累計銷售票數":[],
            "累計銷售金額":[]}#創各年份的dataframe

url = "https://www.tfi.org.tw/BoxOfficeBulletin/weekly/#471"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
sel = '#main-content > section.content > div > section.content.mb-4 > div > div > div > table > tbody > tr > td:nth-child(5) > a'
title = soup.select(sel)


for page in title:
    #if(count1 == 97):
    #    continue
    
    try: #避開那兩個連接給錯的檔名
        items = page["onclick"]
        items.split(",")[1]
        item = items.split('/')[4].split(',')[0].split('.')[0] #處理要輸入的文字
        df = pd.read_excel(".//全國電影票房/" + item + '.xlsx')#讀取excel
        #if item == "全國票房2019年0722-0728統計資訊":
        #    continue
        count = int(len(df))
        for rows in range(count):
            movie_year = str(df.at[rows, "上映日期"]).split('/')[0] #df.at[rows, "上映日期"]藥用str形式，不然獨到有些檔案會出錯(可能有些檔案讀成非文字檔)
            #repitition_data = df.at[rows, "中文片名"].index
           
            
            if movie_year == "2021": #如果是2021年的寫入datayear[0]
                modeselect = 0

            elif movie_year == "2020":
                modeselect = 1
            
            elif movie_year == "2019":
                modeselect = 2
            elif movie_year == "2018":
                modeselect = 3
            elif movie_year == "2017":
                modeselect = 4          #利用modeselect將資料導入對應的年份
            else:
                continue #有些檔案的年份出現#######，過濾掉那些和不在上述範圍的年份
            try:
                repitition_data = datayear[modeselect]["中文片名"].index(str(df.at[rows, "中文片名"])) #過濾重複的部分，只取最新看到的(最新的代表它的值為最大值)
                pass
            except:
                datayear[modeselect]["國別地區"].append(df.at[rows, "國別地區"])
                datayear[modeselect]["中文片名"].append(df.at[rows, "中文片名"])
                datayear[modeselect]["上映日期"].append(df.at[rows, "上映日期"])
                datayear[modeselect]["申請人"].append(df.at[rows, "申請人"])
                #累計銷售票數(df.at[rows, "累計銷售票數"])是str格式
                try: #如果讀出來的數字中有 , 將文字分割後重新合併
                    tmp = df.at[rows, "累計銷售票數"].split(',')
                    tmp2= ''
                    Total_cost_number = tmp2.join(tmp)
                except: #如果沒有，照著原來輸出
                    Total_cost_number = df.at[rows, "累計銷售票數"]

                datayear[modeselect]["累計銷售票數"].append( int(Total_cost_number))
                
                try: #累計銷售金額同理
                    tmp = df.at[rows, "累計銷售金額"].split(',')
                    tmp2= ''
                    Total_cost_number = tmp2.join(tmp)
                except: #如果沒有，照著原來輸出
                    Total_cost_number = df.at[rows, "累計銷售金額"]
               
                datayear[modeselect]["累計銷售金額"].append( int(Total_cost_number) )
            
            

        
    except:
        
        print("file erro!!!!!!!!!!!!!!!", item,  df.at[rows, "累計銷售票數"], tmp, df.at[rows, "中文片名"])
    


score_df = pd.DataFrame.from_dict(datayear[0])
score_df = score_df.sort_values(by = ['累計銷售金額'], ascending=False)
score_df.to_excel('.//2021到2017資料/movies_data_2021.xlsx')

score_df = pd.DataFrame.from_dict(datayear[1])
score_df = score_df.sort_values(by = ['累計銷售金額'], ascending=False)
score_df.to_excel('.//2021到2017資料/movies_data_2020.xlsx')

score_df = pd.DataFrame.from_dict(datayear[2])
score_df = score_df.sort_values(by = ['累計銷售金額'], ascending=False)
score_df.to_excel('.//2021到2017資料/movies_data_2019.xlsx')

score_df = pd.DataFrame.from_dict(datayear[3])
score_df = score_df.sort_values(by = ['累計銷售金額'], ascending=False)
score_df.to_excel('.//2021到2017資料/movies_data_2018.xlsx')

score_df = pd.DataFrame.from_dict(datayear[4])
score_df = score_df.sort_values(by = ['累計銷售金額'], ascending=False)
score_df.to_excel('.//2021到2017資料/movies_data_2017.xlsx')
