from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from movies.models import Tawain_movies_rank_2021, Tawain_movies_rank_2020, Tawain_movies_rank_2019, Tawain_movies_rank_2018, \
Tawain_movies_rank_2017, japan_movies , korea_movies , indea_movies , tai_movies ,  \
    Box_office_champion_year_world , rank_chapion_world , rank_local , documentary_local , scary_movies_local , musical_movies_local , \
        Box_office_champion_year , Box_office_opening_first_week , Single_day_box_office , First_day_box_office ,\
           anime_chapion ,  Box_office_anime_champion_year , Box_office_opening_first_week_anime , box_office_best_tw , rank_local ,\
               Box_office_champion_year_local , Box_office_opening_first_week_local ,First_day_box_office_local


import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

items_2021_data = Tawain_movies_rank_2021.objects.filter(rank__lt=31)
items_2020_data = Tawain_movies_rank_2020.objects.filter(rank__lt=31)
items_2019_data = Tawain_movies_rank_2019.objects.filter(rank__lt=31)
items_2018_data = Tawain_movies_rank_2018.objects.filter(rank__lt=31)
items_2017_data = Tawain_movies_rank_2017.objects.filter(rank__lt=31)
def index(request):
	title_name = "博雅通識小專題:電影資料分析"
	return render(request, 'index.html', locals())
# Create your views here.

def Tawain_movies_rank_2021_show(request):
    items = items_2021_data
    items2 = Tawain_movies_rank_2021.objects.all()
    return render(request, 'Tawain_movies_rank_2021.html', locals())

def Tawain_movies_rank_2020_show(request):
    items = items_2020_data
    items2 = Tawain_movies_rank_2020.objects.all()
    return render(request, 'Tawain_movies_rank_2020.html', locals())

def Tawain_movies_rank_2019_show(request):
    items = items_2019_data
    items2 = Tawain_movies_rank_2019.objects.all()
    return render(request, 'Tawain_movies_rank_2019.html', locals())

def Tawain_movies_rank_2018_show(request):
    items = items_2018_data
    items2 = Tawain_movies_rank_2018.objects.all()
    return render(request, 'Tawain_movies_rank_2018.html', locals())

def Tawain_movies_rank_2017_show(request):
    items = items_2017_data
    items2 = Tawain_movies_rank_2017.objects.all()
    return render(request, 'Tawain_movies_rank_2017.html', locals())
#-------------------------------------------------
def japan(request):
    items = japan_movies.objects.all()
    return render(request, 'japan.html', locals())

def korea(request):
    items = korea_movies.objects.all()
    return render(request, 'korea.html', locals())

def indea(request):
    items = indea_movies.objects.all()
    return render(request, 'indea.html', locals())

def Thailand(request):
    items = tai_movies.objects.all()
    return render(request, 'Thailand.html', locals())

def champofyear(request):
    items = Box_office_champion_year_world.objects.all()
    return render(request, 'champofyear.html', locals())
        
def world50(request):
    items = rank_chapion_world.objects.all()
    return render(request, 'world50.html', locals())
        
def Taiwan(request):
    items = rank_local.objects.all()
    return render(request, 'Taiwan.html', locals()) 

def documentary(request):
    items = documentary_local.objects.all()
    return render(request, 'documentary.html', locals())
        
def scary(request):
    items = scary_movies_local.objects.all()
    return render(request, 'scary.html', locals())
    
def musical(request):
    items = musical_movies_local.objects.all()
    return render(request, 'musical.html', locals())

def Box_office_best_tw_global(request):
    items = box_office_best_tw.objects.all()
    return render(request, 'Box_office_best_tw_global.html', locals())

def Box_office_champion_year_global(request):
    items = Box_office_champion_year.objects.all()
    return render(request, 'Box_office_champion_year_global.html', locals())
    
def Box_office_opening_first_week_global(request):
    items = Box_office_opening_first_week.objects.all()
    return render(request, 'Box_office_opening_first_week_global.html', locals())

def Single_day_box_office_global(request):
    items = Single_day_box_office.objects.all()
    return render(request, 'Single_day_box_office_global.html', locals())

def First_day_box_office_global(request):
    items = First_day_box_office.objects.all()
    return render(request, 'First_day_box_office_global.html', locals())

def anime_chapion_global(request):
    items = anime_chapion.objects.all()
    return render(request, 'anime_chapion_global.html', locals())
    
def Box_office_anime_champion_year_global(request):
    items = Box_office_anime_champion_year.objects.all()
    return render(request, 'Box_office_anime_champion_year_global.html', locals())

def Box_office_opening_first_week_anime_global(request):
    items = Box_office_opening_first_week_anime.objects.all()
    return render(request, 'Box_office_opening_first_week_anime_global.html', locals())

def Box_offic_rank_local(request):
    items = rank_local.objects.all()
    return render(request, 'Box_offic_rank_local.html', locals())

def Box_office_champion_year_tw_local(request):
    items = Box_office_champion_year_local.objects.all()
    return render(request, 'Box_office_champion_year_tw_local.html', locals())
    
def Box_office_opening_first_week_tw_local(request):
    items = Box_office_opening_first_week_local.objects.all()
    return render(request, 'Box_office_opening_first_week_tw_local.html', locals())

def First_day_box_office_tw_local(request):
    items = First_day_box_office_local.objects.all()
    return render(request, 'First_day_box_office_tw_local.html', locals())

#-------------------------------------------------


