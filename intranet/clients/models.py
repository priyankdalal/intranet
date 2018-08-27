from django.db import models
from plans.models import Plans
from zones.models import Zones

# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=10)
    password_string = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    zone = models.IntegerField(blank=True, null=True)
    plan = models.IntegerField(blank=True, null=True)
    region = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=8, blank=True, null=True)
    pan = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    send_sms = models.IntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'
    def get_plans():
        return Plans.objects.all()
    def get_zones():
        return Zones.objects.all()
