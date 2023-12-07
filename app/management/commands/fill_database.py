import requests

from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand

from app.models import NavigationSafetyObjectModel

class Command(BaseCommand):
    help = 'Fill the database with initial data'

    def handle(self, *args, **options):

        url = 'https://plovput.li-st.net/getObjekti/'  

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            for feature in data['features']:
                properties = feature.get('properties', {})
                geometry = feature.get('geometry', {}).get('coordinates', [])

                nav_safety_obj = NavigationSafetyObjectModel(
                    ime=properties.get('naziv_objekta', ''),
                    ps_br = properties.get('ps_br', ''),
                    e_br = properties.get('e_br', ''),
                    tip_objekta = properties.get('tip_objekta', ''),
                    lucka_kapetanija = properties.get('lucka_kapetanija', ''),
                    fotografija = properties.get('fotografija', ''),
                    id_ais = properties.get('id_ais', ''),
                    simbol_oznaka = properties.get('simbol_oznaka', ''),
                    kljuc = properties.get('pk', None),
                    geom=Point(geometry[0], geometry[1]),
                )
                nav_safety_obj.save()

            print('Data fetched and inserted successfully')

        except requests.RequestException as e:
            print(f'Error fetching and inserting data: {e}', status=500)