from django.db import models

class ArithmeticResult(models.Model):
    add = models.IntegerField()
    difference = models.IntegerField()
    product = models.IntegerField()
    quotient = models.FloatField()
    request_time = models.DateTimeField()
    request_ip = models.CharField(max_length=15)
    request_process_time = models.FloatField()