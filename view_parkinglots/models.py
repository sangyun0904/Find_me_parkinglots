from django.db import models

# Create your models here.
class Parkinglot (models.Model):
    
    p_id = models.CharField(("p_id"), max_length=50)
    p_name = models.CharField(("p_name"), max_length=200)
    p_long = models.FloatField(("p_long"))
    p_lat = models.FloatField(("p_lat"))
    p_num = models.IntegerField(("p_num"))
