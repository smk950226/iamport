from django.shortcuts import render
from django.views.generic import ListView
from .models import Item

class ItemListView(ListView):
    model = Item