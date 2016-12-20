from django.shortcuts import render
from django.views.generic.edit import CreateView

# Create your views here.

from models import *

class ItemListView(CreateView):
	model = Item
	template_name = "karaoke/create_item.html"
	fields = ['noms','url','comentari']

