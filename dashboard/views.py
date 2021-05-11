import datetime

from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Subquery, OuterRef, F, Sum

from .models import Entry


def home(request):
    return render(request, template_name="home.html")


def linechart(request):
    countries = [
        "United Kingdom",
        "Germany",
        "France",
        "Israel",
        "United States",
        "India",
        "Brazil",
        "Turkey",
        "Chile",
        "Russia",
    ]
    cutoff_date = datetime.datetime.today() - datetime.timedelta(days=60)
    datasets = []
    for country in countries:
        qs = Entry.objects.filter(country=country, date__gte=cutoff_date)
        data = [
            {"x": entry.date, "y": entry.people_vaccinated_per_hundred} for entry in qs
        ]
        datasets.append({"label": country, "data": data})
    return JsonResponse(data={"datasets": datasets})


def piechart(request):
    total_vaccines = Entry.objects.all().aggregate(Sum("daily_vaccinations"))[
        "daily_vaccinations__sum"
    ]
    qs = (
        Entry.objects.values("vaccines")
        .annotate(total=Sum("daily_vaccinations"))
        .order_by("-total")[:9]
    )
    # calculate percentage and rest
    combinations = {
        entry["vaccines"]: (entry["total"] / total_vaccines) for entry in qs
    }
    combinations["other"] = 1 - sum(entry["total"] for entry in qs) / total_vaccines
    return JsonResponse(data={"combinations": combinations})


def table(request):
    last_date = Entry.objects.order_by("-date").first().date
    qs = Entry.objects.all()
    sq = qs.filter(country=OuterRef("country")).order_by("-date").values("id")
    qs2 = (
        qs.filter(date__gte=last_date - datetime.timedelta(days=5))
        .annotate(latest=Subquery(sq[:1]))
        .filter(id=F("latest"))
        .order_by("-people_vaccinated_per_hundred")
    )
    return JsonResponse(data={"data": list(qs2.values())})
