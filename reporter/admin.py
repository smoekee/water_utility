from django.contrib import admin
from .models import Incidences
from django.contrib.gis.geos import Point
from datetime import datetime
from leaflet.admin import LeafletGeoAdmin
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

from reporter.models import WaterConsumption

# Register your models here.

class IncidencesAdmin(admin.ModelAdmin):
    list_display = ('name','location')


admin.site.register(Incidences, IncidencesAdmin)

class WaterConsumptionAdmin(LeafletGeoAdmin):
    pass

admin.site.register(WaterConsumption, WaterConsumptionAdmin)


df_excelReader = pd.read_excel("/home/smoki/geodjango/agricom/waterwatch_clean2.xlsx")

# print(df_excelReader.head())

for index, row in df_excelReader.iterrows():
    Id = index
    Suburb = row['Suburb']
    NoOfSingleResProp = row['Number of single-residential properties_number']
    AvgMonthlyKL = row['Oct 2017\nkl/month']
    AvgMonthlyKLPredicted = 0
    PredictionAccuracy = 0
    Month = row['Month']
    Year = row['Yearadf']
    DateTime = datetime.now()
    Longitude = row['Longitude']
    Latitude = row['Latitude']


    WaterConsumption(Id=Id, Suburb=Suburb,NoOfSingleResProp = NoOfSingleResProp,
                     AvgMonthlyKL=AvgMonthlyKL, AvgMonthlyKLPredicted=AvgMonthlyKLPredicted,
                     PredictionAccuracy=PredictionAccuracy, Month=Month, Year=Year,
                     DateTime=DateTime, geom=Point(Longitude, Latitude)).save()