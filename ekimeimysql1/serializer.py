from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import Prefecture, Railway_type, Company, Line, Station, LineService, StationService, Category, Creator, YoutubeChannel, Name, Artist, Song, Vocal, Movie, Part, StationInMovie


class StationServiceSerializer(serializers.ModelSerializer):
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

class StationSearchSerializer(serializers.ModelSerializer):
	line_service_name = serializers.CharField(source='line_service_code')
	class Meta:
		model = StationService
		fields = ['__str__', 'station_service_code', 'line_service_name']

class StationInMovieSerializer(serializers.ModelSerializer):
	station_group_code = serializers.IntegerField(source='station_service_code.station_code.station_group_code')
	line_service_code = serializers.CharField(source='station_service_code.line_service_code.line_service_code')
	line_service_name = serializers.CharField(source='station_service_code.line_service_code.__str__')
	pref = serializers.CharField(source='station_service_code.station_code.pref_code')
	class Meta:
		model = StationInMovie
		fields = ['station_group_code', 'station_service_name', 'station_service_code', 'line_service_code', 'line_service_name', 'pref']

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