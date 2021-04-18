import datetime

from django.shortcuts import render
from django.http import JsonResponse

from .models import Entry

def home(request):
    return render(request, template_name='home.html')

def linechart(request):
    countries=["United Kingdom", "Germany", "France", "Israel", "United States", "India", "Brazil", "Turkey", "Chile", "Russia"]
    cutoff_date = datetime.datetime.today() - datetime.timedelta(days=60)
    datasets = []
    for country in countries:
        qs = Entry.objects.filter(country=country, date__gte=cutoff_date)
        data = [{'x': entry.date, 'y': entry.people_vaccinated_per_hundred} for entry in qs]
        datasets.append({'label': country, 'data': data})
    return JsonResponse(data={'datasets': datasets})