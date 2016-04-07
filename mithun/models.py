from __future__ import unicode_literals

from django.db import models


class Dreamreal(models.Model):

   website = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   name = models.CharField(max_length = 50)
   phonenumber = models.IntegerField()

   class Meta:
      db_table = "dreamreal"
   def __unicode__(self):
	return self.website

class Dream(models.Model):

   web = models.CharField(max_length = 50)
   ma = models.CharField(max_length = 50)
   na = models.CharField(max_length = 50)
   ph = models.IntegerField()

   class Meta:
      db_table = "dream"

class Drems(models.Model):
    #id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'drems'
