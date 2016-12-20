from __future__ import unicode_literals

from django.db import models

from datetime import datetime

# Create your models here.


class Item(models.Model):
	noms = models.CharField(max_length=200,help_text="Els cantants que van a triomfar")
	url = models.URLField(max_length=300,help_text="Link al YouTube, Vimeo o altres")
	data = models.DateTimeField( default=datetime.now() )
	comentari = models.TextField(blank=True)

