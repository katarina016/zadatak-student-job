from django.contrib.gis.db import models

class NavigationSafetyObjectModel(models.Model):
    ime = models.CharField(max_length=255, null=False, blank=False)
    ps_br = models.CharField(max_length=255, null=True, blank=True)
    e_br = models.CharField(max_length=255, null=True, blank=True)
    tip_objekta = models.IntegerField(null=True, blank=True)
    lucka_kapetanija = models.CharField(max_length=255, null=True, blank=True)
    fotografija = models.CharField(max_length=255, null=True, blank=True)
    id_ais = models.CharField(max_length=255, null=True, blank=True)
    simbol_oznaka = models.CharField(max_length=255, null=True, blank=True)
    kljuc = models.IntegerField(primary_key=True)
    geom = models.PointField(srid=4326)

    def __str__(self):
        return self.ime
    
    class Meta:
        app_label = ''
        db_table = 'navigation_safety_object'
