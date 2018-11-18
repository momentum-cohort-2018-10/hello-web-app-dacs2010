from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect
from collection.forms import ThingForm
from collection.models import Thing


# Create your views here.
def index(request):
    number = 6
    things = Thing.objects.all()
    return render(request, 'index.html', {
        "things": things,
    })


# def image_upload(request):
#     if request.method == 'POST':
#         image = ImageF


def thing_detail(request, slug):
    thing = Thing.objects.get(slug=slug)
    return render(request, "things/thing_detail.html", {
        "thing": thing,
    })


def edit_thing(request, slug):
    thing = Thing.objects.get(slug=slug)
    form_class = ThingForm
    if request.method == 'POST':       
        form = form_class(data=request.POST, instance=thing)
        if form.is_valid():
            form.save()
            return redirect('thing_detail', slug=thing.slug)
    else:
        form = form_class(instance=thing)
    return render(request, 'things/edit_thing.html', {
        'thing': thing,
        'form': form,
    })


def create_thing(request):
    form_class = ThingForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            thing = form.save(commit=False)
            thing.user = request.user
            thing.slug = slugify(thing.name)
            thing.save()
            return redirect('thing_detail', slug=thing.slug)
    else:
        form = form_class()
    return render(request, 'things/create_thing.html', {
        'form': form,
    })
