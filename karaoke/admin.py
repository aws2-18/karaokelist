from django.contrib import admin

# Register your models here.

from models import *

class ItemAdmin(admin.ModelAdmin):
	model = Item
	list_display = ['noms','tema','show_url','data','fet']
	list_editable = ['fet']
	ordering = ('fet','data')
	def show_url(self,obj):
		return '<a href="%s">%s</a>' % (obj.url, obj.url)
	show_url.allow_tags = True

admin.site.register(Item,ItemAdmin)

