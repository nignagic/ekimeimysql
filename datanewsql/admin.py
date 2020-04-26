from django.contrib import admin

# Register your models here.
from .models import Railway_type, Country, Region, Prefecture, Company, Line, Station, LineService, StationService, MovieCategory, Creator, YoutubeChannel, Name, Artist, Song, Vocal, Movie, Part, StationInMovie

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