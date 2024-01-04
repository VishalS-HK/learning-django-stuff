from django.shortcuts import render
from .models import Destinations
# Create your views here.
def index(request):
    # dest1 = Destinations()
    # dest1.name = 'Mumbai'
    # dest1.desc = 'The City that never sleeps.'
    # dest1.price = 679
    # dest1.img = 'destination_1.jpg'
    # dest1.offer = False

    # dest2 = Destinations()
    # dest2.name = 'Hyderabad'
    # dest2.desc = 'First Biryani, then Sherwani.'
    # dest2.price = 700
    # dest2.img = 'destination_2.jpg'
    # dest2.offer = True

    # dest3 = Destinations()
    # dest3.name = 'Hyderabad'
    # dest3.desc = 'Silicon Valley of India.'
    # dest3.price = 750
    # dest3.img = 'destination_3.jpg'
    # dest3.offer = False

    # dests = [dest1, dest2, dest3]
    dests = Destinations.objects.all()
    return render(request, "index.html", {'dests': dests})
