from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from .models import Railway_type, Country, Region, Prefecture, Company, Line, Station, LineService, StationService, MovieCategory, Creator, YoutubeChannel, Name, Artist, Song, Vocal, Movie, Part, StationInMovie

class StationServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = StationService
		fields = ('station_name', 'station_service_code', 'line_service_code')

class LineServiceSerializer(serializers.ModelSerializer):
	line_name = serializers.CharField(source='__str__')
	class Meta:
		model = LineService
		fields = ('line_name', 'line_service_code')

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
	line_service_code = serializers.IntegerField(source='station_service_code.line_service_code.line_service_code')
	line_name = serializers.CharField(source='station_service_code.line_service_code.__str__')
	pref = serializers.CharField(source='station_service_code.station_code.pref_code.pref_name')
	class Meta:
		model = StationInMovie
		fields = ['station_name', 'station_service_code', 'station_group_code', 'line_service_code', 'line_name', 'pref']

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