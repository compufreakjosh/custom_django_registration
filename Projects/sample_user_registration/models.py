#coding=utf-8

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

def_max_length = 255

class City(models.Model):	
	name = models.CharField(max_length=def_max_length)
	
	class Meta:
		app_label = "sample_user_registration"
		verbose_name = "City"
		verbose_name_plural = "Cities"
		
	def __unicode__(self):
		return "%s" % self.name
		

class Profile(models.Model):
	user = models.ForeignKey(User, unique=True)	
	city = models.ForeignKey(City, null=True, blank=True, db_index=True)	
	
	class Meta:
		app_label = "sample_user_registration"
		verbose_name = "User profile"
		verbose_name_plural = "User profiles"	
	
try:
	admin.site.register(Profile)
	admin.site.register(City)	
except:
	pass
