from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from .models import Railway_type, Country, Region, Prefecture, Company, Line, Station, LineService, StationService, MovieCategory, Creator, YoutubeChannel, Name, Artist, Song, Vocal, Movie, Part, StationInMovie

class StationServiceSerializer(serializers.ModelSerializer):
	line_service_code = serializers.CharField(source='line_service_code.line_service_code')
	class Meta:
		model = StationService
		fields = ('__str__', 'station_service_code', 'line_service_code')

class LineServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = LineService
		fields = ('__str__', 'line_service_code')

# class TransferSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Line
# 		fields = ('line_name', 'line_cd')

class StationServiceSearchSerializer(serializers.ModelSerializer):
	class Meta:
		model = StationService
		fields = ['station_name', 'station_service_code', 'line_service_code']

class StationInMovieSerializer(serializers.ModelSerializer):
	station_group_code = serializers.IntegerField(source='station_service_code.station_code.station_group_code')
	line_service_code = serializers.CharField(source='station_service_code.line_service_code.line_service_code')
	line_service_name = serializers.CharField(source='station_service_code.line_service_code')
	pref = serializers.CharField(source='station_service_code.station_code.pref_code.pref_name')
	class Meta:
		model = StationInMovie
		fields = ['station_sung_name', 'station_service_code', 'station_group_code', 'line_service_code', 'line_service_name', 'pref']

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