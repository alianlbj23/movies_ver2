from django.urls import path
from django.contrib import admin
from movies.views import index, Tawain_movies_rank_2021_show,  Tawain_movies_rank_2020_show, Tawain_movies_rank_2019_show, Tawain_movies_rank_2018_show, Tawain_movies_rank_2017_show, \
    index,  japan , korea , indea , Thailand , champofyear , world50 , Taiwan , documentary , scary , \
       musical , Box_office_best_tw_global , Box_office_opening_first_week_global , Single_day_box_office_global , First_day_box_office_global,\
           anime_chapion_global , Box_office_anime_champion_year_global , Box_office_opening_first_week_anime_global , Box_office_champion_year_global ,\
               Box_offic_rank_local , Box_office_champion_year_tw_local , Box_office_opening_first_week_tw_local , First_day_box_office_tw_local
urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('Tawain_movies_rank_2021_show/' , Tawain_movies_rank_2021_show),
    path('Tawain_movies_rank_2020_show/' , Tawain_movies_rank_2020_show),
    path('Tawain_movies_rank_2019_show/' , Tawain_movies_rank_2019_show),
    path('Tawain_movies_rank_2018_show/' , Tawain_movies_rank_2018_show),
    path('Tawain_movies_rank_2017_show/' , Tawain_movies_rank_2017_show),
    path('japan/' , japan),
    path('korea/' , korea),
    path('indea/' , indea),
    path('Thailand/' , Thailand),
    path('champofyear/' , champofyear),
    path('world50/' , world50),   
    path('Taiwan/' , Taiwan), 
    path('documentary/' , documentary),
    path('scary/' , scary), 
    path('musical/' , musical), 
    path('Box_office_best_tw_global/' , Box_office_best_tw_global),  
    path('Box_office_champion_year_global/' , Box_office_champion_year_global), 
    path('Box_office_opening_first_week_global/' , Box_office_opening_first_week_global),
    path('Single_day_box_office_global/' , Single_day_box_office_global),   
    path('First_day_box_office_global/' , First_day_box_office_global), 
    path('anime_chapion_global/' , anime_chapion_global),
    path('Box_office_anime_champion_year_global/' , Box_office_anime_champion_year_global), 
    path('Box_office_opening_first_week_anime_global/' , Box_office_opening_first_week_anime_global), 
    path('Box_offic_rank_local/' , Box_offic_rank_local), 
    path('Box_office_champion_year_tw_local/' , Box_office_champion_year_tw_local), 
    path('Box_office_opening_first_week_tw_local/' , Box_office_opening_first_week_tw_local), 
    path('First_day_box_office_tw_local/' , First_day_box_office_tw_local),
]