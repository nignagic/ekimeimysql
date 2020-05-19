from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from .models import Railway_type, Country, Region, Prefecture, Company, Line, Station, LineService, StationService, MovieCategory, Creator, YoutubeChannel, Name, Artist, Song, Vocal, Movie, Part, StationInMovie

class StationServiceSerializer(serializers.ModelSerializer):
	line_service_pk = serializers.IntegerField(source='line_service.id')
	line_service_name = serializers.CharField(source='line_service.line_service_name')
	station_service_pk = serializers.IntegerField(source='id')
	class Meta:
		model = StationService
		fields = ('__str__', 'station_service_pk', 'line_service_pk', 'line_service_name', 'get_color')

class StationSerializer(serializers.ModelSerializer):
	line_pk = serializers.IntegerField(source='line.id')
	line_name = serializers.CharField(source='line.line_name')
	station_pk = serializers.IntegerField(source='id')
	class Meta:
		model = StationService
		fields = ('__str__', 'station_pk', 'line_pk', 'line_name')

class LineServiceSerializer(serializers.ModelSerializer):
	line_service_pk = serializers.IntegerField(source='id')
	class Meta:
		model = LineService
		fields = ('__str__', 'line_service_pk')

# class TransferSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Line
# 		fields = ('line_name', 'line_cd')

# class StationServiceSearchSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = StationService
# 		fields = ['station_name', 'station_service', 'line_service']

class StationInMovieSerializer(serializers.ModelSerializer):
	station_service_pk = serializers.IntegerField(source='station_service.id')
	station_group_code = serializers.IntegerField(source='station_service.station.station_group_code')
	line_service_pk = serializers.IntegerField(source='station_service.line_service.pk')
	line_service_name = serializers.CharField(source='station_service.line_service')
	pref = serializers.CharField(source='station_service.station.pref_code.pref_name')
	get_color = serializers.CharField(source='station_service.get_color')
	class Meta:
		model = StationInMovie
		fields = ['station_sung_name', 'station_service_pk', 'station_group_code', 'line_service_pk', 'line_service_name', 'pref', 'get_color', 'back_rel']

class NameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Name
		fields = ['id', 'name']

class SongSerializer(serializers.ModelSerializer):
	class Meta:
		model = Song
		fields = ['id', 'name']

class VocalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vocal
		fields = ['id', 'name']