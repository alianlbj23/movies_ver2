from django.db import models
from django.utils import timezone



class box_office_best_tw(models.Model): #排行榜
    rank = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    box_office = models.CharField(max_length=1000)
    year = models.CharField(max_length=1000)
    area = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
   
class anime_chapion(models.Model): #動畫票房冠軍 
    rank = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    box_office = models.CharField(max_length=1000)
    year = models.CharField(max_length=1000)
    area = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

#-----------------------------------------------------------------以上欄位相同 0, 13
class Box_office_champion_year(models.Model): #年度票房冠軍 
    year = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    box_office = models.CharField(max_length=1000)
    area = models.CharField(max_length=100)    
    pub_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

class Box_office_anime_champion_year(models.Model): #年度票房冠軍(動畫) 
    year = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    box_office = models.CharField(max_length=1000)
    area = models.CharField(max_length=100)    
    pub_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name    
#-----------------------------------------------------------------以上欄位相同 1, 14

class Box_office_opening_first_week(models.Model): #首週開片票房 
    rank = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    days = models.CharField(max_length=100)
    box_office = models.CharField(max_length=1000)
    year = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name    

class Box_office_opening_first_week_local(models.Model): #首週開片票房(本土) 
    rank = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    days = models.CharField(max_length=100)
    box_office = models.CharField(max_length=1000)
    year = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name 

class Box_office_opening_first_week_anime(models.Model): #首週開片票房(動畫) 
    rank = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    days = models.CharField(max_length=100)
    box_office = models.CharField(max_length=1000)
    year = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name 
#-----------------------------------------------------------------以上欄位相同 2, 7, 15
class Single_day_box_office(models.Model): #單日票房
    rank = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    box_office = models.CharField(max_length=1000)
    weeks = models.CharField(max_length=100)
    year = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name 

class First_day_box_office(models.Model): #首日票房
    rank = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    box_office = models.CharField(max_length=1000)
    weeks = models.CharField(max_length=100)
    year = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name 

class First_day_box_office_local(models.Model): #首日票房(本土)
    rank = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    box_office = models.CharField(max_length=1000)
    weeks = models.CharField(max_length=100)
    year = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name 
#-----------------------------------------------------------------3, 4, 8

class rank_local(models.Model): #首日票房(本土)
    rank = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    box_office = models.CharField(max_length=1000)
    year = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name 

class documentary_local (models.Model): #紀錄片(本土)
    rank = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    box_office = models.CharField(max_length=1000)
    year = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name 

class  scary_movies_local (models.Model): #驚悚片(本土)
    rank = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    box_office = models.CharField(max_length=1000)
    year = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name 

class  musical_movies_local (models.Model): #歌舞片(本土)
    rank = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    box_office = models.CharField(max_length=1000)
    year = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name 

class  japan_movies (models.Model): #日本
    rank = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    box_office = models.CharField(max_length=1000)
    year = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name 

class  korea_movies (models.Model): #韓國
    rank = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    box_office = models.CharField(max_length=1000)
    year = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name 

class  indea_movies (models.Model): #印度
    rank = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    box_office = models.CharField(max_length=1000)
    year = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name 

class  tai_movies (models.Model): #泰國
    rank = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    box_office = models.CharField(max_length=1000)
    year = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name 

#-----------------------------------------------------------------5, 9, 10, 11, 12, 16, 17, 18, 19
class Box_office_champion_year_local (models.Model): #年度票房冠軍(本土)
    year = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    box_office = models.CharField(max_length=1000)    
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
#------------------------------------------------------------------------in tw end

class rank_chapion_world (models.Model): #全球排行
    rank = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    box_office = models.CharField(max_length=1000)  
    year = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

#------------------------------------------------------------------------0

class Box_office_champion_year_world (models.Model): #全球年度票房冠軍
    year = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    box_office = models.CharField(max_length=1000)  
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

#------------------------------------------------------------------------Taiwan movies 2021 rank START
class Tawain_movies_rank_2021(models.Model):
    rank = models.PositiveIntegerField(default=0)
    area = area = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    dates = models.CharField(max_length=1000)
    applicant = models.CharField(max_length=1000)
    tickets = models.PositiveIntegerField(default=0)
    Total_Sale_Figure = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name


#------------------------------------------------------------------------Taiwan movies rank END

#------------------------------------------------------------------------Taiwan movies 2020 rank START
class Tawain_movies_rank_2020(models.Model):
    rank = models.PositiveIntegerField(default=0)
    area = area = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    dates = models.CharField(max_length=1000)
    applicant = models.CharField(max_length=1000)
    tickets = models.PositiveIntegerField(default=0)
    Total_Sale_Figure =models.PositiveIntegerField(default=0)

#------------------------------------------------------------------------Taiwan movies rank END

#------------------------------------------------------------------------Taiwan movies 2019 rank START
class Tawain_movies_rank_2019(models.Model):
    rank = models.PositiveIntegerField(default=0)
    area = area = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    dates = models.CharField(max_length=1000)
    applicant = models.CharField(max_length=1000)
    tickets = models.PositiveIntegerField(default=0)
    Total_Sale_Figure = models.PositiveIntegerField(default=0)

#------------------------------------------------------------------------Taiwan movies rank END

#------------------------------------------------------------------------Taiwan movies 2018 rank START
class Tawain_movies_rank_2018(models.Model):
    rank = models.PositiveIntegerField(default=0)
    area = area = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    dates = models.CharField(max_length=1000)
    applicant = models.CharField(max_length=1000)
    tickets = models.PositiveIntegerField(default=0)
    Total_Sale_Figure = models.PositiveIntegerField(default=0)

#------------------------------------------------------------------------Taiwan movies rank END

#------------------------------------------------------------------------Taiwan movies 2017 rank START
class Tawain_movies_rank_2017(models.Model):
    rank = models.PositiveIntegerField(default=0)
    area = area = models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    dates = models.CharField(max_length=1000)
    applicant = models.CharField(max_length=1000)
    tickets = models.PositiveIntegerField(default=0)
    Total_Sale_Figure = models.PositiveIntegerField(default=0)

#------------------------------------------------------------------------Taiwan movies rank END