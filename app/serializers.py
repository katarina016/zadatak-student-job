from rest_framework import serializers
from django.contrib.gis.geos import Point

from .models import NavigationSafetyObjectModel

class NavigationSafetyObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationSafetyObjectModel
        fields = '__all__'
        
    def to_representation(self, instance):
        return {
            'properties': {
                'naziv_objekta': instance.ime,
                'ps_br': instance.ps_br,
                'e_br': instance.e_br,
                'tip_objekta': instance.tip_objekta,
                'lucka_kapetanija': instance.lucka_kapetanija,
                'fotografija': instance.fotografija,
                'id_ais': instance.id_ais,
                'simbol_oznaka': instance.simbol_oznaka,
                'pk': instance.kljuc,
            },
            'geometry': {
                'type': 'Point',
                'coordinates': [instance.geom.x, instance.geom.y]
            }
        }
    
    def to_internal_value(self, data):
        properties = data.get('properties', {})
        geometry = data.get('geometry', {}).get('coordinates', [])

        nav_safety_object_data = {
            'ime': properties.get('naziv_objekta', ''),
            'ps_br': properties.get('ps_br', ''),
            'e_br': properties.get('e_br', ''),
            'tip_objekta': properties.get('tip_objekta', ''),
            'lucka_kapetanija': properties.get('lucka_kapetanija', ''),
            'fotografija': properties.get('fotografija', ''),
            'id_ais': properties.get('id_ais', ''),
            'simbol_oznaka': properties.get('simbol_oznaka', ''),
            'kljuc': properties.get('pk', None),
            'geom': Point(geometry[0], geometry[1]),
        }
                
        return nav_safety_object_data
