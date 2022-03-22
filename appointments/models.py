from django.db import models
from datetime import datetime, timedelta
import uuid
# Create your models here.
class DateTime(models.Model):
    date = models.DateField(unique=True)
    fromTime = models.TimeField()
    fromTo = models.TimeField()

class Services(models.Model):

    Service_TYPE_CHOICES = (("Dental", 'Dental'),("ENT", 'ENT'),("Nephro", 'Nephro'))
    service = models.CharField(choices=Service_TYPE_CHOICES,default="Dental",max_length=20,blank=True,null=True)
    freq = models.CharField(max_length=10,null=True,blank=True)



    # def save(self):
    #     d = timedelta(days=1)
    #     self.date = self.date + d
    #     self.fromTime = self.fromTime
    #     self.fromTo = self.fromTo
    #     super(DateTime, self).save()

class Appointment(models.Model):
    appointId = models.UUIDField( primary_key = True,default = uuid.uuid4,editable = False)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    service = models.CharField(max_length=50, null=True, blank=True)
    STATUS_CHOICES = ((1, 'Confirm'),(2, 'Cancel'),(3, 'Pending'), )
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES,default=1)

