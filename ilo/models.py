from django.db import models

# Create your models here.

class IloHost(models.Model):
  host_name = models.CharField(max_length=100)
  address = models.CharField(max_length=100)
  username = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  
  def __unicode__(self):
    return self.host_name
