from django.contrib import admin

# Register your models here.

from models import *

class ItemAdmin(admin.ModelAdmin):
	model = Item
	list_display = ['noms','tema','show_url','data','fet']
	list_editable = ['fet']
	ordering = ('fet','data')
	def show_url(self,obj):
		return '<a title="%s" href="%s" target="_blank">%s</a>' % (obj.comentari, obj.url, obj.url)
	show_url.allow_tags = True

class VotAdmin(admin.ModelAdmin):
	model = Vot
	list_display = ['item','ip','data']

admin.site.register(Item,ItemAdmin)
admin.site.register(Vot,VotAdmin)
