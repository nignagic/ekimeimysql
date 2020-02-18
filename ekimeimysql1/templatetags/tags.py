from django import template
from ekimeimysql1.models import StationService
register = template.Library()

@register.filter(name='get_station_service_code')
def get_station_service_code(value):
	return StationService.objects.get(station_service_code=value)