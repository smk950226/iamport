from django.shortcuts import render
from django.views.generic import ListView
from .models import Item

class ItemListView(ListView):
    model = Item

    def get_queryset(self):
        self.q = self.request.GET.get('q', '')

        qs = super().get_queryset()
        
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.qs
        return context