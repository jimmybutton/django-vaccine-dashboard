from django.db import models

class Entry(models.Model):
    country = models.CharField(max_length=200)
    iso_code = models.CharField(max_length=3, null=True, blank=True)
    date = models.DateField()
    total_vaccinations = models.IntegerField(null=True, blank=True)
    people_vaccinated = models.IntegerField(null=True, blank=True)
    people_fully_vaccinated = models.IntegerField(null=True, blank=True)
    daily_vaccinations_raw = models.IntegerField(null=True, blank=True)
    daily_vaccinations = models.IntegerField(null=True, blank=True)
    total_vaccinations_per_hundred = models.FloatField(null=True, blank=True)
    people_vaccinated_per_hundred = models.FloatField(null=True, blank=True)
    people_fully_vaccinated_per_hundred = models.FloatField(null=True, blank=True)
    daily_vaccinations_per_million = models.IntegerField(null=True, blank=True)
    vaccines = models.CharField(max_length=200, null=True, blank=True)
    source_name = models.CharField(max_length=200, null=True, blank=True)
    source_website = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.country} {self.date}"
    
    class Meta:
        verbose_name_plural = "entries"
