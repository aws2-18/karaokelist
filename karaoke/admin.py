from django.contrib import admin

# Register your models here.

from models import *

class ItemAdmin(admin.ModelAdmin):
	model = Item
	list_display = ['noms','show_url','data']
	def show_url(self,obj):
		return '<a href="%s">%s</a>' % (obj.url, obj.url)
	show_url.allow_tags = True

admin.site.register(Item,ItemAdmin)
