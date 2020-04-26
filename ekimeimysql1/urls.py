from django.urls import path
from django.conf.urls import url, include
from . import views

from rest_framework import routers
router = routers.DefaultRouter()
urlpatterns = router.urls

app_name = 'ekimeimysql1'

urlpatterns = [
	path('', views.Top.as_view(), name='top'),
	path('login/', views.Login.as_view(), name='login'),
	path('logout/', views.Logout.as_view(), name='logout'),
	path('list/', views.MovieListView.as_view(), name="list"),
	path('detail/<slug:main_id>/', views.detail_movie, name='detail'),
	# path('lineservice/<slug:line_service_code>/', views.StationServiceListbyLineView.as_view(), name='stationservicelistbylineview'),
	path('linelist/', views.LineServiceListbyCompanyView.as_view(), name='lineservicelistbycompanyview'),
	path('stationsearch/', views.StationServiceSearchView.as_view(), name='stationsearchview'),
	path('song/<int:id>/', views.MovieListbySongView.as_view(), name='song_list'),
	path('vocal/<int:id>/', views.MovieListbyVocalView.as_view(), name='vocal_list'),
	path('register/', views.MovieRegisterView.as_view(), name='register'),
	path('edit/<slug:main_id>/part/', views.movie_part_edit, name='part_edit'),
	path('edit/<slug:main_id>/part/<int:part_num>/', views.movie_part_station_edit, name='station_edit'),
	path('popup/song_create/', views.PopupSongCreate.as_view(), name='popup_song_create'),
	path('popup/artist_create/', views.PopupArtistCreate.as_view(), name='popup_artist_create'),
	path('popup/vocal_create/', views.PopupVocalCreate.as_view(), name='popup_vocal_create'),
	
	path('railwaysearch/', views.RegionListView.as_view(), name='railwaysearch'),
	path('region/<int:pk>', views.CompanyListbyRegionView.as_view(), name='companylistbyregion'),
	path('company/<int:pk>', views.LineServiceListbyCompanyView.as_view(), name='lineservicelistbycompany'),
	path('pref/<int:pk>', views.LineServiceListbyPrefectureView.as_view(), name='lineservicelistbyprefecture'),


	path('line/<int:line_code>/', views.StationListbyLineView.as_view(), name='stationlistbylineview'),
	# path('lineservice/<slug:line_service_code>/', views.StationServiceListbyLineView.as_view(), name='stationservicelistbylineview'),
	path('lineservice/<slug:line_service_code>/', views.MovieListbyLineServiceView.as_view(), name='movielistbylineservice'),
	path('linelist/', views.LineServiceListbyCompanyView.as_view(), name='lineservicelistbycompanyview'),
	path('stationservice/<int:station_service_code>/', views.MovieListbyStationServiceView.as_view(), name='movielistbystationservice'),
	path('stationsearch/', views.StationSearchView.as_view(), name='stationsearchview'),
	
	path('uploadrailwaytype/', views.uploadRailwayType, name='uploadRailwayType'),
	path('uploadcountry/', views.uploadCountry, name='uploadCountry'),
	path('uploadregion/', views.uploadRegion, name='uploadRegion'),
	path('uploadprefecture/', views.uploadPrefecture, name='uploadPrefecture'),
	path('uploadcompany/', views.uploadCompany, name='uploadCompany'),
	path('uploadline/', views.uploadLine, name='uploadLine'),
	path('upload/', views.uploadStation, name='uploadStation'),
	path('uploadlineservice/', views.uploadLineService, name='uploadLineService'),
	path('uploadstationservice/', views.uploadStationService, name='uploadStationService'),
	path('companydelete/', views.CompanyDelete, name='CompanyDelete'),
	path('linedelete/', views.LineDelete, name='LineDelete'),
	path('stationdelete/', views.StationDelete, name='StationDelete'),
	path('lineservicedelete/', views.LineServiceDelete, name='LineServiceDelete'),
	path('stationservicedelete/', views.StationServiceDelete, name='StationServiceDelete'),
	path('lineprefset/', views.lineprefset, name='lineprefset'),
	path('lineserviceprefset/', views.lineserviceprefset, name='lineserviceprefset'),

	path('notice/', views.NoticeView.as_view(), name='notice'),
	
	url('^api/line/(?P<pref_code>.+)/$', views.LineServiceViewSet.as_view()),
	url('^api/station/(?P<line_service_code>.+)/$', views.StationServiceViewSet.as_view()),
	url('^api/stationsearch/(?P<words>.+)/$', views.StationServiceSearchViewSet.as_view()),
	url('^api/transfer/(?P<station_service_code>.+)/$', views.TransferViewSet.as_view()),
	url('^api/partstation/(?P<id>.+)/$', views.PartStationViewSet.as_view()),
	url('api/name/', views.NameViewSet.as_view()),
	url('api/song/', views.SongViewSet.as_view()),
	url('api/vocal/', views.VocalViewSet.as_view()),
]