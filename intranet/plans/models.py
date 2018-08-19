from django.db import models

# Create your models here.
class Plans(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    discount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plans'