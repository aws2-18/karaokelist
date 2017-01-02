from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

# Create your views here.

from karaoke.models import *

# generic class-based views
# https://docs.djangoproject.com/en/1.10/topics/class-based-views/
# https://docs.djangoproject.com/en/1.10/ref/class-based-views/generic-display/
# https://docs.djangoproject.com/en/1.10/ref/class-based-views/generic-editing/

class ItemCreateView(CreateView):
	model = Item
	# indiquem la plantilla personalitzada i els camps que han d'apareixer al formulari
	# veureu que la plantilla es molt senzilla ja que fa tot el formulari amb {{form.as_p}}
	template_name = "karaoke/create_item.html"
	fields = ['noms','tema','url','comentari']


class ItemListView(ListView):
	model = Item
	# si no posem template_name agafara per defecte karaoke/item_list.html
	def get_queryset(self):
		# nomes posem els items que estiguin per cantar
		return Item.objects.filter(fet=False)

class VotaView(ListView):
	model = Item
	template_name = "karaoke/vota.html"
	def get_queryset(self):
		# nomes mostrem els items que ja s'hagin cantat i puguin ser votats
		return Item.objects.filter(fet=True)


# view classica procedimental amb render
from ipware.ip import get_ip

def votaActionView(request,votacio):
	print( votacio )
	item = Item.objects.get(id=votacio)
	if item:
		ip = get_ip(request)
		if not ip:
			ip = "desconeguda"
		try:
			votrepe = Vot.objects.filter( ip=ip, item=item )
			if votrepe:
				return render(request, 'karaoke/vota_fail.html')
		except:
			pass
		vot = Vot( item=item, ip=ip )
		vot.save()
		return render(request, 'karaoke/vota_success.html')
	return render(request, 'karaoke/vota_fail.html')

