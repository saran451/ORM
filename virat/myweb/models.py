
from django.db import models
from django.contrib import admin
class client_DB(models.Model):
    noplate_no=models.CharField(max_length=10)
    name=models.CharField(max_length=15)
    address=models.TextField()
    servicetype=models.CharField(max_length=20)
    phonenum=models.IntegerField()
    bikemodel=models.CharField(max_length=15)
    nextserviceduedate=models.DateField()

class client_DBAdmin(admin.ModelAdmin):
    list_display=["noplate_no","name","address","servicetype","bikemodel","nextserviceduedate","phonenum"]

