from django.db import models

# Create your models here.
class Zones(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'zones'
