from django.db import models
from django.utils import timezone

# Create your models here.
class Run(models.Model):
    id_run = models.AutoField(primary_key=True)
    run_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField( default=timezone.now)
    total_time = models.CharField(max_length=200)
    distance = models.FloatField()