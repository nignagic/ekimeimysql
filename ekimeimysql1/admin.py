from django.contrib import admin
from .models import Railway_type, Country, Region, Prefecture, Company, BelongsCategory, NameCategory, Line, Station, LineService, StationService, MovieCategory, Creator, YoutubeChannel, Name, Artist, Song, Vocal, Movie, Part, StationInMovie, LineInMovie, MovieUpdateInformation

# Register your models here.

# class StationServiceAdmin(admin.ModelAdmin):
# 	list_display = ('id', 'station_cd', 'station_name', 'line_cd', 'add', 'e_sort')
# 	list_editable = ['e_sort']
# 	search_fields = ['station_name']

# class StationInMovieAdmin(admin.ModelAdmin):
# 	list_display = ('id', 'id_in_movie', 'station_cd', 'station_name')
# 	search_fields = ['station_name']

# class MovieAdmin(admin.ModelAdmin):
# 	list_display = ('title', 'channel', 'main_id', 'published_at', 'is_collab')

admin.site.register(Railway_type)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Prefecture)
admin.site.register(Company)
admin.site.register(Line)
admin.site.register(Station)
admin.site.register(LineService)
admin.site.register(StationService)
admin.site.register(MovieCategory)
admin.site.register(Creator)
admin.site.register(YoutubeChannel)
admin.site.register(Name)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Vocal)
admin.site.register(Movie)
admin.site.register(Part)
admin.site.register(StationInMovie)
admin.site.register(LineInMovie)
admin.site.register(BelongsCategory)
admin.site.register(MovieUpdateInformation)