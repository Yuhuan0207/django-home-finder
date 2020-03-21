from django.shortcuts import render
from django.views import generic
from .models import Location

class IndexView(generic.ListView):
    template_name = 'homesapp/index.html'

    def get_queryset(self):
        return Location.objects.all()

class LocationView(generic.DetailView):
    template_name = 'homesapp/location_detail.html'
    model = Location