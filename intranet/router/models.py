from django.db import models

# Create your models here.
class Routers(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'routers'
