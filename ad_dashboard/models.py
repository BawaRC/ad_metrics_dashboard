from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    finish_date = models.DateField()
    responsible = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AdCampaign(models.Model):
    name = models.CharField(max_length=100)
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    conversions = models.IntegerField()
    cost = models.FloatField()

    @property
    def ctr(self):
        return (self.clicks / self.impressions) * 100 if self.impressions > 0 else 0

    @property
    def conversion_rate(self):
        return (self.conversions / self.clicks) * 100 if self.clicks > 0 else 0

    @property
    def roi(self):
        return ((self.conversions * 10 - self.cost) / self.cost) * 100 if self.cost > 0 else 0

    def __str__(self):
        return self.name
        