from django.urls import path
from django.conf.urls import url, include
from . import views

from rest_framework import routers
router = routers.DefaultRouter()
# router.register('station', views.StationViewSet)
# router.register('line/<int:pref_cd>', views.LineViewSet.as_view(), base_name='lines')
urlpatterns = router.urls

app_name = 'datanewsql'

urlpatterns = [
	path('line/<int:line_code>/', views.StationListbyLineView.as_view(), name='stationlistbylineview'),
	path('lineservice/<slug:line_service_code>/', views.StationServiceListbyLineView.as_view(), name='stationservicelistbylineview'),
	path('linelist/', views.LineServiceListbyCompanyView.as_view(), name='lineservicelistbycompanyview'),
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

	path('notice/', views.NoticeView.as_view(), name='notice'),


	path('list/', views.MovieListView.as_view(), name="list"),
	path('detail/<slug:main_id>/', views.detail_movie, name='detail'),
	path('line/<int:line_cd>/', views.MovieListbyLineView.as_view(), name='line_list'),
	path('station/<int:station_cd>/', views.MovieListbyStationView.as_view(), name='station_list'),
	path('song/<int:id>/', views.MovieListbySongView.as_view(), name='song_list'),
	path('vocal/<int:id>/', views.MovieListbyVocalView.as_view(), name='vocal_list'),
	path('register/', views.MovieRegisterView.as_view(), name='register'),
	path('edit/<slug:main_id>/part/', views.part_edit, name='part_edit'),
	path('edit/<slug:main_id>/part/<int:part_num>/', views.station_edit, name='station_edit'),
	# path('lineprefset/', views.lineprefset, name='lineprefset'),
	url('^api/line/(?P<pref_cd>.+)/$', views.LineServiceViewSet.as_view()),
	url('^api/station/(?P<line_cd>.+)/$', views.StationServiceViewSet.as_view()),
	url('^api/stationsearch/(?P<words>.+)/$', views.StationServiceSearchViewSet.as_view()),
	# url('^api/transfer/(?P<station_cd>.+)/$', views.TransferViewSet.as_view()),
	url('^api/partstation/(?P<id>.+)/$', views.PartStationViewSet.as_view()),
	url('api/name/', views.NameViewSet.as_view()),
	url('api/song/', views.SongViewSet.as_view()),
	url('api/vocal/', views.VocalViewSet.as_view()),
]