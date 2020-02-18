from django.contrib import admin
from .models import Prefecture, Railway_type, Company, Line, Station, LineService, StationService, Category, Creator, YoutubeChannel, Name, Artist, Song, Vocal, Movie, Part, StationInMovie

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

admin.site.register(Prefecture)
admin.site.register(Line)
admin.site.register(LineService)
admin.site.register(Station)
admin.site.register(StationService)
admin.site.register(Category)
admin.site.register(Creator)
admin.site.register(YoutubeChannel)
admin.site.register(Name)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Vocal)
admin.site.register(Movie)
admin.site.register(Part)
admin.site.register(StationInMovie)