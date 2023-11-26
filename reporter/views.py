from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime
from django.core.serializers import serialize
from reporter.models import WaterConsumption
from django.template.context import Context
import pandas as pd

# Create your views here.
def home(request):
    """ Renders home page """
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page'
        }
    )