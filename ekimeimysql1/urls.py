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
	path('stationsearch/', views.StationServiceSearchView.as_view(), name='stationsearch'),
	path('artist/', views.ArtistListView.as_view(), name="artistlist"),
	path('song/', views.SongListView.as_view(), name="songlist"),
	path('vocal/', views.VocalListView.as_view(), name="vocallist"),
	path('creator/', views.CreatorTopView.as_view(), name="creatortop"),
	path('channel/', views.ChannelListView.as_view(), name="channellist"),

	path('songtop/', views.SongTopView.as_view(), name='songtop'),
	path('song/<int:id>/', views.MovieListbySongView.as_view(), name='movielistbysong'),
	path('artist/<int:id>/', views.MovieListbyArtistView.as_view(), name='movielistbyartist'),
	path('vocal/<int:id>/', views.MovieListbyVocalView.as_view(), name='movielistbyvocal'),
	path('creator/<int:id>/', views.EachCreatorView.as_view(), name='eachcreator'),
	path('name/<int:id>/', views.MovieListbyNameView.as_view(), name='movielistbyname'),
	path('channel/<slug:channel_id>/', views.MovieListbyChannelView.as_view(), name='movielistbychannel'),
	path('register/', views.MovieRegisterView.as_view(), name='register'),
	path('edit/<slug:main_id>/part/', views.movie_part_edit, name='part_edit'),
	path('edit/<slug:main_id>/part/<int:part_num>/', views.movie_part_station_edit, name='station_edit'),
	path('popup/song_create/', views.PopupSongCreate.as_view(), name='popup_song_create'),
	path('popup/artist_create/', views.PopupArtistCreate.as_view(), name='popup_artist_create'),
	path('popup/vocal_create/', views.PopupVocalCreate.as_view(), name='popup_vocal_create'),
	
	path('railwaytop/', views.RailwayTopView.as_view(), name='railwaytop'),
	path('category/<int:pk>', views.LineServiceListbyCategoryView.as_view(), name='lineservicelistbycategory'),
	path('region/<int:pk>', views.CompanyListbyRegionView.as_view(), name='companylistbyregion'),
	path('company/<int:pk>', views.LineServiceListbyCompanyView.as_view(), name='lineservicelistbycompany'),
	path('pref/<int:pk>', views.LineServiceListbyPrefectureView.as_view(), name='lineservicelistbyprefecture'),


	path('line/<int:line_pk>/', views.MovieListbyLineView.as_view(), name='movielistbyline'),
	path('station/<int:station_pk>/', views.MovieListbyStationView.as_view(), name='movielistbystation'),
	# path('lineservice/<slug:line_service_code>/', views.StationServiceListbyLineView.as_view(), name='stationservicelistbylineview'),
	path('lineservice/<int:line_service_pk>/', views.MovieListbyLineServiceView.as_view(), name='movielistbylineservice'),
	path('linelist/', views.LineServiceListbyCompanyView.as_view(), name='lineservicelistbycompanyview'),
	path('stationservice/<int:station_service_pk>/', views.MovieListbyStationServiceView.as_view(), name='movielistbystationservice'),
	
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
	path('stationservicegroupcodeset/', views.Stationservicegroupcodeset, name='stationservicegroupcodeset'),
	path('lineservicelineset/', views.lineservicelineset, name='lineservicelineset'),

	path('emergency/', views.EmergencyCode, name='emergency'),

	path('companyregister/', views.CompanyRegisterView.as_view(), name='companyregister'),
	path('lineregister/<int:company_pk>', views.LineRegisterView, name='lineregister'),
	path('stationregister/<int:line_pk>', views.StationRegisterView, name='stationregister'),
	path('lineserviceregister/<int:company_pk>', views.LineServiceRegisterView, name='lineserviceregister'),
	path('stationserviceregister/<int:line_service_pk>', views.StationServiceRegisterView, name='stationserviceregister'),


	path('stationserviceexport/', views.StationServiceExport, name='stationserviceexport'),


	path('notice/', views.NoticeView.as_view(), name='notice'),
	
	url('^api/line/(?P<pref_code>.+)/$', views.LineServiceViewSet.as_view()),
	url('^api/stationservice/(?P<line_service_pk>.+)/$', views.StationServiceViewSet.as_view()),
	url('^api/station/(?P<line_pk>.+)/$', views.StationViewSet.as_view()),
	url('^api/stationsearch/(?P<words>.+)/$', views.StationServiceSearchViewSet.as_view()),
	url('^api/transfer/(?P<station_service_pk>.+)/$', views.TransferViewSet.as_view()),
	url('^api/partstation/(?P<id>.+)/$', views.PartStationViewSet.as_view()),
	url('api/name/', views.NameViewSet.as_view()),
	url('api/song/', views.SongViewSet.as_view()),
	url('api/vocal/', views.VocalViewSet.as_view()),
]