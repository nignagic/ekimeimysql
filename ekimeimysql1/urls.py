from django.urls import path
from django.conf.urls import url, include
from . import views

from rest_framework import routers
router = routers.DefaultRouter()
urlpatterns = router.urls

app_name = 'ekimeimysql1'

urlpatterns = [
	path('', views.Top.as_view(), name='top'),
	path('list/', views.MovieListView.as_view(), name="list"),
	path('detail/<slug:main_id>/', views.detail_movie, name='detail'),
	path('lineservice/<slug:line_service_code>/', views.StationServiceListbyLineView.as_view(), name='stationservicelistbylineview'),
	path('linelist/', views.LineServiceListbyCompanyView.as_view(), name='lineservicelistbycompanyview'),
	path('stationsearch/', views.StationServiceSearchView.as_view(), name='stationsearchview'),
	# path('station/<int:station_cd>/', views.MovieListbyStationView.as_view(), name='station_list'),
	path('song/<int:id>/', views.MovieListbySongView.as_view(), name='song_list'),
	path('vocal/<int:id>/', views.MovieListbyVocalView.as_view(), name='vocal_list'),
	path('register/', views.MovieRegisterView.as_view(), name='register'),
	path('edit/<slug:main_id>/part/', views.movie_part_edit, name='part_edit'),
	path('edit/<slug:main_id>/part/<int:part_num>/', views.movie_part_station_edit, name='station_edit'),
	path('popup/song_create/', views.PopupSongCreate.as_view(), name='popup_song_create'),
	path('popup/artist_create/', views.PopupArtistCreate.as_view(), name='popup_artist_create'),
	path('popup/vocal_create/', views.PopupVocalCreate.as_view(), name='popup_vocal_create'),
	path('upload/', views.uploadStation, name='uploadStation'),
	path('uploadline/', views.uploadLine, name='uploadLine'),
	path('uploadcompany/', views.uploadCompany, name='uploadCompany'),
	path('uploadrailwaytype/', views.uploadRailwayType, name='uploadRailwayType'),
	path('uploadpref/', views.uploadPref, name='uploadPref'),
	path('uploadstationservice/', views.uploadStationService, name='uploadStationService'),
	path('uploadlineservice/', views.uploadLineService, name='uploadLineService'),
	path('stationdelete/', views.StationDelete, name='StationDelete'),
	path('linedelete/', views.LineDelete, name='LineDelete'),
	path('companydelete/', views.CompanyDelete, name='CompanyDelete'),
	path('stationservicedelete/', views.StationServiceDelete, name='StationServiceDelete'),
	path('lineservicedelete/', views.LineServiceDelete, name='LineServiceDelete'),
	path('lineprefset/', views.lineprefset, name='lineprefset'),
	path('lineserviceprefset/', views.lineServiceprefset, name='lineserviceprefset'),
	url('^api/line/(?P<pref_code>.+)/$', views.LineServiceViewSet.as_view()),
	url('^api/station/(?P<line_cd>.+)/$', views.StationServiceViewSet.as_view()),
	url('^api/stationsearch/(?P<words>.+)/$', views.StationServiceSearchViewSet.as_view()),
	# url('^api/transfer/(?P<station_cd>.+)/$', views.TransferViewSet.as_view()),
	url('^api/partstation/(?P<id>.+)/$', views.PartStationViewSet.as_view()),
	url('api/name/', views.NameViewSet.as_view()),
	url('api/song/', views.SongViewSet.as_view()),
	url('api/vocal/', views.VocalViewSet.as_view()),
]