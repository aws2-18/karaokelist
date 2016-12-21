from __future__ import unicode_literals

from django.db import models
import django

from datetime import datetime


# Create your models here.


class Item(models.Model):
	noms = models.CharField(max_length=200,help_text="Els cantants que van a triomfar")
	tema = models.CharField(max_length=200,help_text="Tema que cantareu")
	url = models.URLField(max_length=300,help_text="Link al YouTube, Vimeo o altres")
	data = models.DateTimeField( default=django.utils.timezone.now )
	fet = models.BooleanField(default=False)
	comentari = models.TextField(blank=True)
	#ip = models.CharField(blank=True,null=True,default=get_ip(request))
	def __str__(self):
		return str(self.noms)+" | "+str(self.tema)

class Vot(models.Model):
	item = models.ForeignKey(Item)
	ip = models.CharField(max_length=20)
	comentari = models.TextField(blank=True)
	data = models.DateTimeField( default=django.utils.timezone.now )
	def __str__(self):
		return str(self.item)

