from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

def singleobj(request):
    data = Person.objects.get(id=1)
    serilaizer = PersonSerializer(data)
    json_data = JSONRenderer().render(serilaizer.data)
    return HttpResponse(json_data, 
                        content_type='application/json')

def multiobj(request):
    data = Person.objects.all()
    serilaizer = PersonSerializer(data,many=True)
    json_data = JSONRenderer().render(serilaizer.data)
    return HttpResponse(json_data, 
                        content_type='application/json')