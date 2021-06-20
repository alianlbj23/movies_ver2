#panda讀維基百科後寫入，有好幾種不同的表格，第一個大表格編號從0開始
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
#觀察到用panda處理，每個table都是一個list
#panda處理
import pandas as pd
url = "https://zh.wikipedia.org/wiki/%E5%8F%B0%E7%81%A3%E6%9C%80%E9%AB%98%E9%9B%BB%E5%BD%B1%E7%A5%A8%E6%88%BF%E6%94%B6%E5%85%A5%E5%88%97%E8%A1%A8#%E6%8E%92%E8%A1%8C%E6%A6%9C"
#台灣上映的電影
df = pd.read_html(url) #讀取url

from movies.models import box_office_best_tw, anime_chapion

#0和13的表格欄位一樣
movie_dic = {0:box_office_best_tw, 13:anime_chapion}
for j, z in zip(movie_dic, movie_dic.values()): #j讀陣列，z讀movielist
    df2 = df[j] #讀取總體排行榜
    count = len(df2) #抓有幾個row
    q = z.objects.all() #讓q取得box_office_best_tw的東西
    if q.count() == 0 : #如果q算出來，裡面東西為0，做
        for i in range(count):
            
            newdata = z(rank = str(df2.iloc[i][0]), name = str(df2.iloc[i][1]), box_office = str(df2.iloc[i][2]),
                                        year = str(df2.iloc[i][3]), area = str(df2.iloc[i][4]),            )
            newdata.save()

#1,14
from movies.models import Box_office_champion_year, Box_office_anime_champion_year
movie_dic = {1:Box_office_champion_year, 14:Box_office_anime_champion_year}
for j, z in zip(movie_dic, movie_dic.values()): #j讀陣列，z讀movielist
    df2 = df[j] #讀取總體排行榜
    count = len(df2) #抓有幾個row
    q = z.objects.all() #讓q取得box_office_best_tw的東西
    if q.count() == 0 : #如果q算出來，裡面東西為0，做
        for i in range(count):
            
            newdata = z(year = str(df2.iloc[i][0]), name = str(df2.iloc[i][1]), box_office = str(df2.iloc[i][2]),
                                        area = str(df2.iloc[i][3]),            )
            newdata.save()

#2, 7, 15
from movies.models import Box_office_opening_first_week, Box_office_opening_first_week_local, Box_office_opening_first_week_anime
movie_dic = {2:Box_office_opening_first_week, 7:Box_office_opening_first_week_local, 15:Box_office_opening_first_week_anime}
for j, z in zip(movie_dic, movie_dic.values()): #j讀陣列，z讀movielist
    df2 = df[j] #讀取總體排行榜
    count = len(df2) #抓有幾個row
    q = z.objects.all() #讓q取得box_office_best_tw的東西
    if q.count() == 0 : #如果q算出來，裡面東西為0，做
        for i in range(count):
            
            newdata = z(rank = str(df2.iloc[i][0]), name = str(df2.iloc[i][1]), days = str(df2.iloc[i][2]),
                        box_office = str(df2.iloc[i][3]), year = str(df2.iloc[i][4]))
            newdata.save()

 
#3, 4, 8
from movies.models import Single_day_box_office, First_day_box_office, First_day_box_office_local
movie_dic = {3:Single_day_box_office, 4:First_day_box_office, 8:First_day_box_office_local}
for j, z in zip(movie_dic, movie_dic.values()): #j讀陣列，z讀movielist
    df2 = df[j] #讀取總體排行榜
    count = len(df2) #抓有幾個row
    q = z.objects.all() #讓q取得box_office_best_tw的東西
    if q.count() == 0 : #如果q算出來，裡面東西為0，做
        for i in range(count):
            
            newdata = z(rank = str(df2.iloc[i][0]), name = str(df2.iloc[i][1]), box_office = str(df2.iloc[i][2]),
                        weeks = str(df2.iloc[i][3]), year = str(df2.iloc[i][4]))
            newdata.save()

#5, 9, 10, 11, 16, 17, 18, 19
from movies.models import rank_local, documentary_local, scary_movies_local, musical_movies_local
from movies.models import japan_movies, korea_movies, indea_movies, tai_movies
movie_dic = {5:rank_local, 9:documentary_local, 10:scary_movies_local, 11:musical_movies_local, 16:japan_movies, 
             17:korea_movies, 18:indea_movies, 19:tai_movies}
for j, z in zip(movie_dic, movie_dic.values()): #j讀陣列，z讀movielist
    df2 = df[j] #讀取總體排行榜
    count = len(df2) #抓有幾個row
    q = z.objects.all() #讓q取得box_office_best_tw的東西
    if q.count() == 0 : #如果q算出來，裡面東西為0，做
        for i in range(count):
            
            newdata = z(rank = str(df2.iloc[i][0]), name = str(df2.iloc[i][1]), box_office = str(df2.iloc[i][2]),
                        year = str(df2.iloc[i][4]))
            newdata.save()

#6
from movies.models import Box_office_champion_year_local 
movie_dic = {6:Box_office_champion_year_local}
for j, z in zip(movie_dic, movie_dic.values()): #j讀陣列，z讀movielist
    df2 = df[j] #讀取總體排行榜
    count = len(df2) #抓有幾個row
    q = z.objects.all() #讓q取得box_office_best_tw的東西
    if q.count() == 0 : #如果q算出來，裡面東西為0，做
        for i in range(count):
            
            newdata = z(year = str(df2.iloc[i][0]), name = str(df2.iloc[i][1]), box_office = str(df2.iloc[i][2]),)
            newdata.save()

#-------------------------------------------------end tw

#-------------------------------------------------global
url = "https://zh.wikipedia.org/wiki/%E5%85%A8%E7%90%83%E6%9C%80%E9%AB%98%E9%9B%BB%E5%BD%B1%E7%A5%A8%E6%88%BF%E6%94%B6%E5%85%A5%E5%88%97%E8%A1%A8"
#全球
df = pd.read_html(url) #讀取url

#0
from movies.models import rank_chapion_world
movie_dic = {0:rank_chapion_world}
for j, z in zip(movie_dic, movie_dic.values()): #j讀陣列，z讀movielist
    df2 = df[j] #讀取總體排行榜
    count = len(df2) #抓有幾個row
    q = z.objects.all() #讓q取得box_office_best_tw的東西
    if q.count() == 0 : #如果q算出來，裡面東西為0，做
        for i in range(count):
            
            newdata = z(rank = str(df2.iloc[i][0]), name = str(df2.iloc[i][1]), box_office = str(df2.iloc[i][2]),year =str(df2.iloc[i][3]) )
            newdata.save()

#2
from movies.models import Box_office_champion_year_world
movie_dic = {2:Box_office_champion_year_world}
for j, z in zip(movie_dic, movie_dic.values()): #j讀陣列，z讀movielist
    df2 = df[j] #讀取總體排行榜
    count = len(df2) #抓有幾個row
    q = z.objects.all() #讓q取得box_office_best_tw的東西
    if q.count() == 0 : #如果q算出來，裡面東西為0，做(代表裡面沒資料)(避免資料重複輸入)
        for i in range(count):
            
            newdata = z(year = str(df2.iloc[i][0]), name = str(df2.iloc[i][1]), box_office = str(df2.iloc[i][2]), )
            newdata.save()
#-------------------------------------------------global end


#-------------------------------------------------taiwan movie rank 2021 START  
from movies.models import Tawain_movies_rank_2021
df = pd.read_excel('.//2021到2017資料/movies_data_2021.xlsx')
count = int(len(df))
q = Tawain_movies_rank_2021.objects.all()
q.delete()
if q.count() == 0:
    for rows in range(count):
        newdata = Tawain_movies_rank_2021(rank = str(rows + 1), area = str(df.at[rows, "國別地區"]), name = str(df.at[rows, "中文片名"]),
                                        dates = str(df.at[rows, "上映日期"]),applicant = str(df.at[rows, "申請人"]), tickets = df.at[rows, "累計銷售票數"], 
                                        Total_Sale_Figure = df.at[rows, "累計銷售金額"],)
        newdata.save()


#-------------------------------------------------taiwan movie rank 2021 END

#-------------------------------------------------taiwan movie rank 2020 START  
from movies.models import Tawain_movies_rank_2020
df = pd.read_excel('.//2021到2017資料/movies_data_2020.xlsx')
count = int(len(df))
q = Tawain_movies_rank_2020.objects.all()
q.delete()
if q.count() == 0:
    for rows in range(count):
        newdata = Tawain_movies_rank_2020(rank = str(rows + 1), area = str(df.at[rows, "國別地區"]), name = str(df.at[rows, "中文片名"]),
                                        dates = str(df.at[rows, "上映日期"]),applicant = str(df.at[rows, "申請人"]), tickets = df.at[rows, "累計銷售票數"], 
                                        Total_Sale_Figure = df.at[rows, "累計銷售金額"],)
        newdata.save()


#-------------------------------------------------taiwan movie rank 2020 END

#-------------------------------------------------taiwan movie rank 2019 START  
from movies.models import Tawain_movies_rank_2019
df = pd.read_excel('.//2021到2017資料/movies_data_2019.xlsx')
count = int(len(df))
q = Tawain_movies_rank_2019.objects.all()
q.delete()
print(q)
if q.count() == 0:
    for rows in range(count):
        newdata = Tawain_movies_rank_2019(rank = str(rows + 1), area = str(df.at[rows, "國別地區"]), name = str(df.at[rows, "中文片名"]),
                                        dates = str(df.at[rows, "上映日期"]),applicant = str(df.at[rows, "申請人"]), tickets = df.at[rows, "累計銷售票數"], 
                                        Total_Sale_Figure = df.at[rows, "累計銷售金額"],)
        newdata.save()


#-------------------------------------------------taiwan movie rank 2019 END

#-------------------------------------------------taiwan movie rank 2018 START  
from movies.models import Tawain_movies_rank_2018
df = pd.read_excel('.//2021到2017資料/movies_data_2018.xlsx')
count = int(len(df))
q = Tawain_movies_rank_2018.objects.all()
#q.delete()
#print(q)
if q.count() == 0:
    for rows in range(count):
        newdata = Tawain_movies_rank_2018(rank = str(rows + 1), area = str(df.at[rows, "國別地區"]), name = str(df.at[rows, "中文片名"]),
                                        dates = str(df.at[rows, "上映日期"]),applicant = str(df.at[rows, "申請人"]), tickets = df.at[rows, "累計銷售票數"], 
                                        Total_Sale_Figure = df.at[rows, "累計銷售金額"],)
        newdata.save()


#-------------------------------------------------taiwan movie rank 2018 END

#-------------------------------------------------taiwan movie rank 2017 START  
from movies.models import Tawain_movies_rank_2017
df = pd.read_excel('.//2021到2017資料/movies_data_2017.xlsx')
count = int(len(df))
q = Tawain_movies_rank_2017.objects.all()
#q.delete()
#print(q)
if q.count() == 0:
    for rows in range(count):
        newdata = Tawain_movies_rank_2017(rank = str(rows + 1), area = str(df.at[rows, "國別地區"]), name = str(df.at[rows, "中文片名"]),
                                        dates = str(df.at[rows, "上映日期"]),applicant = str(df.at[rows, "申請人"]), tickets = df.at[rows, "累計銷售票數"], 
                                        Total_Sale_Figure = df.at[rows, "累計銷售金額"],)
        newdata.save()


#-------------------------------------------------taiwan movie rank 2017 END
