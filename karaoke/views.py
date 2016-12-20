from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

# Create your views here.

from models import *


class ItemCreateView(CreateView):
	model = Item
	template_name = "karaoke/create_item.html"
	fields = ['noms','tema','url','comentari']


class ItemListView(ListView):
	model = Item
	def get_queryset(self):
		return Item.objects.filter(fet=False)

def successView(request):
	return render(request, 'karaoke/success.html')
