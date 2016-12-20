from django.shortcuts import render
from django.views.generic.edit import CreateView

# Create your views here.

from models import *

class ItemListView(CreateView):
	model = Item
	fields = ['noms','url','comentari','fet']


def index(request):
	return render(request, "create_item.html", {'form',ItemListView})
