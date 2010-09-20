from django.db import models
from auth_test.core.models import CustomUser

class Project(models.Model):
    date_started = models.DateField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    super_admin = models.ForeignKey(CustomUser)
    license = models.CharField(max_length=50)
    progess = models.FloatField(default=0)
    web_site = models.URLField()
#   super_admin, moder, ...
    
    