from django.db import models
import datetime

class Members(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

# class Membership(models.Model):
#   start_date = models.DateField(default='2000-01-01')
#   expire_date = models.DateField()
  
#   class Meta:
#     ordering = ["expire_date"]

#   def save(self, *args, **kwargs):
#     if self.expire_date is None:
#       self.expire_date = self.start_date.date() + datetime.timedelta(days=30)
#       super(Membership, self).save(*args, **kwargs)

# # idea for automatically calculated date from: https://stackoverflow.com/questions/54657667/django-how-to-add-2-days-to-an-existing-date-entered-by-user

class Created(models.Model):
  day = models.DateField(default='2000-01-01')