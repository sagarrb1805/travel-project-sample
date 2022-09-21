from django.http import HttpResponse
from django.shortcuts import render
from . models import Place, Person

# Create your views here.
def home(request):
    obj = Place.objects.all()
    person_obj = Person.objects.all()

    return render(request, 'index.html', {'result':obj, 'people':person_obj})

def privacy(request):
    return render(request, 'privacy-policy.html')
