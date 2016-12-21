from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

# Create your views here.

from models import *

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
		return Item.objects.filter(fet=False)


# view classica procedimental amb render (no la utilitzem, nomes com a exemple)

def successView(request):
	return render(request, 'karaoke/success.html')
