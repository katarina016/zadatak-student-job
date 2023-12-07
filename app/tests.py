from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.gis.geos import Point
from django.core.management import call_command

from .models import NavigationSafetyObjectModel

class NavigationSafetyObjectTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.sample_object = NavigationSafetyObjectModel.objects.create(
            ime="Otočić Mrtovnjak",
            ps_br="390",
            e_br="E3115",
            tip_objekta=11,
            lucka_kapetanija="Zadar",
            fotografija="fotografije/773.jpg",
            id_ais=None,  
            simbol_oznaka="/media/simboli/2.png",
            kljuc=773,
            geom=Point(15.17517, 44.01113)
        )

    def test_get_one_object(self):
        
        response = self.client.get('app/api/navigation-safety-object/773/')
        print(response)
        self.assertEqual(response.status_code, 200)

        expected_data = {
            "properties": {
                "naziv_objekta": "Otočić Mrtovnjak",
                "ps_br": "390",
                "e_br": "E3115",
                "tip_objekta": 11,
                "lucka_kapetanija": "Zadar",
                "fotografija": "fotografije/773.jpg",
                "id_ais": None,
                "simbol_oznaka": "/media/simboli/2.png",
                "pk": 773
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    15.17517,
                    44.01113
                ]
            }
        }
        self.assertEqual(response.json(), expected_data)