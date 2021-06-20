from django.contrib import admin
from .models import box_office_best_tw, anime_chapion

class listAdmin(admin.ModelAdmin):
    list_display = ('rank', 'name', 'box_office', 'year', 'area', 'pub_date')

admin.site.register(box_office_best_tw, listAdmin)
admin.site.register(anime_chapion, listAdmin)
#----------------------------------------------------------0, 13
from .models import Box_office_champion_year, Box_office_anime_champion_year
class Box_office_champion_yearAdmin(admin.ModelAdmin):
    list_display = ('year', 'name', 'box_office', 'area')

admin.site.register(Box_office_champion_year, Box_office_champion_yearAdmin)
admin.site.register(Box_office_anime_champion_year, Box_office_champion_yearAdmin)
#-----------------------------------------------------------------------------------1, 14

from .models import Box_office_opening_first_week, Box_office_opening_first_week_local, Box_office_opening_first_week_anime
class Box_office_opening_first_weekAdmin(admin.ModelAdmin):
    list_display = ('rank', 'name', 'days', 'box_office', 'year')

admin.site.register(Box_office_opening_first_week, Box_office_opening_first_weekAdmin)
admin.site.register(Box_office_opening_first_week_local, Box_office_opening_first_weekAdmin)
admin.site.register(Box_office_opening_first_week_anime, Box_office_opening_first_weekAdmin)

#-----------------------------------------------------------------------------------2, 7, 15


from .models import Single_day_box_office, First_day_box_office, First_day_box_office_local
class Single_day_box_officeAdmin(admin.ModelAdmin):
    list_display = ('rank', 'name', 'box_office', 'weeks', 'year')

admin.site.register(Single_day_box_office, Single_day_box_officeAdmin)
admin.site.register(First_day_box_office, Single_day_box_officeAdmin)
admin.site.register(First_day_box_office_local, Single_day_box_officeAdmin)
#-----------------------------------------------------------------------------------3, 4, 8

from .models import rank_local, documentary_local, scary_movies_local, musical_movies_local
from .models import japan_movies, korea_movies, indea_movies, tai_movies
class rank_localAdmin(admin.ModelAdmin):
    list_display = ('rank', 'name', 'box_office', 'year')

admin.site.register(rank_local, rank_localAdmin)
admin.site.register(documentary_local, rank_localAdmin)
admin.site.register(scary_movies_local, rank_localAdmin)
admin.site.register(musical_movies_local, rank_localAdmin)
admin.site.register(japan_movies, rank_localAdmin)
admin.site.register(korea_movies, rank_localAdmin)
admin.site.register(indea_movies, rank_localAdmin)
admin.site.register(tai_movies, rank_localAdmin)
#-----------------------------------------------------------------------------------3, 4, 8
from .models import Box_office_champion_year_local
class Box_office_champion_year_localAdmin(admin.ModelAdmin):
    list_display = ('year', 'name', 'box_office')

admin.site.register(Box_office_champion_year_local, Box_office_champion_year_localAdmin)
# Register your models here.
#-----------------------------------------------------------------------------------end tw

#-----------------------------------------------------------------------------------global
from .models import rank_chapion_world
class rank_chapion_worldAdmin(admin.ModelAdmin):
    list_display = ('rank', 'name', 'box_office', 'year')

admin.site.register(rank_chapion_world, rank_chapion_worldAdmin)

#-----------------------------------------------------------------------------------0
from .models import Box_office_champion_year_world
class Box_office_champion_year_worldAdmin(admin.ModelAdmin):
    list_display = ('year', 'name', 'box_office')

admin.site.register(Box_office_champion_year_world, Box_office_champion_year_worldAdmin)
#-----------------------------------------------------------------------------------2

#------------------------------------------------------------------------Taiwan movies 2021 rank START
from .models import Tawain_movies_rank_2021
class Tawain_movies_rank_2021Admin(admin.ModelAdmin):
    list_display = ('rank', 'area', 'name', 'dates', 'applicant', 'tickets', 'Total_Sale_Figure')

admin.site.register(Tawain_movies_rank_2021, Tawain_movies_rank_2021Admin)
#------------------------------------------------------------------------Taiwan movies rank END

#------------------------------------------------------------------------Taiwan movies 2020 rank START
from .models import Tawain_movies_rank_2020
class Tawain_movies_rank_2020Admin(admin.ModelAdmin):
    list_display = ('rank', 'area', 'name', 'dates', 'applicant', 'tickets', 'Total_Sale_Figure')

admin.site.register(Tawain_movies_rank_2020, Tawain_movies_rank_2020Admin)
#------------------------------------------------------------------------Taiwan movies rank END

#------------------------------------------------------------------------Taiwan movies 2019 rank START
from .models import Tawain_movies_rank_2019
class Tawain_movies_rank_2019Admin(admin.ModelAdmin):
    list_display = ('rank', 'area', 'name', 'dates', 'applicant', 'tickets', 'Total_Sale_Figure')

admin.site.register(Tawain_movies_rank_2019, Tawain_movies_rank_2019Admin)
#------------------------------------------------------------------------Taiwan movies rank END

#------------------------------------------------------------------------Taiwan movies 2018 rank START
from .models import Tawain_movies_rank_2018
class Tawain_movies_rank_2018Admin(admin.ModelAdmin):
    list_display = ('rank', 'area', 'name', 'dates', 'applicant', 'tickets', 'Total_Sale_Figure')

admin.site.register(Tawain_movies_rank_2018, Tawain_movies_rank_2018Admin)
#------------------------------------------------------------------------Taiwan movies rank END

#------------------------------------------------------------------------Taiwan movies 2017 rank START
from .models import Tawain_movies_rank_2017
class Tawain_movies_rank_2017Admin(admin.ModelAdmin):
    list_display = ('rank', 'area', 'name', 'dates', 'applicant', 'tickets', 'Total_Sale_Figure')

admin.site.register(Tawain_movies_rank_2017, Tawain_movies_rank_2017Admin)
#------------------------------------------------------------------------Taiwan movies rank END