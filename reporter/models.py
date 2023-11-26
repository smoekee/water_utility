#from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural =" Incidences" 

class WaterConsumption(models.Model):
    Id = models.IntegerField(primary_key=True)
    Suburb = models.CharField(max_length=100)
    NoOfSingleResProp = models.IntegerField()
    AvgMonthlyKL = models.IntegerField()
    AvgMonthlyKLPredicted = models.IntegerField()
    PredictionAccuracy = models.IntegerField()
    Month = models.CharField(max_length=50)
    Year = models.IntegerField()
    DateTime = models.DateTimeField()
    geom = models.PointField()

    def __str__(self):
        return self.Suburb

    class Meta:
        verbose_name_plural = 'WaterConsumption'