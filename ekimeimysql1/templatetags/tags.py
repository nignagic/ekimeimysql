from django import template
from ekimeimysql1.models import StationService
register = template.Library()

@register.filter(name='get_station_service')
def get_station_service(value):
	return StationService.objects.get(pk=value)