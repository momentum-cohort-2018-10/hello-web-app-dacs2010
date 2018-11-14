from django.shortcuts import render
from collection.models import Thing

# Create your views here.
def index(request):
    number = 6
    things = Thing.objects.all()
    return render(request, 'index.html', {
        'number': number,
        "things": things,
    })