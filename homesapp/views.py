from django.shortcuts import render
from django.views import generic
from .models import Location, Property

class IndexView(generic.ListView):
    template_name = 'homesapp/index.html'

    def get_queryset(self):
        return Location.objects.all()


class LocationView(generic.DetailView):
    template_name = 'homesapp/location_detail.html'
    model = Location


class PropertyView(generic.DetailView):
    template_name = 'homesapp/property_detail.html'
    model = Property