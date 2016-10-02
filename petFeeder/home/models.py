from django.db import models

# Create your models here.
class Date(models.Model):
        feed = models.CharField(max_length=5,)
        pub_date = models.DateTimeField('date published')
