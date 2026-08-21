from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
# Create your views here.

def singleobj(request):
    data = Person.objects.get(id=1)
    serilaizer = PersonSerializer(data)
    print(serilaizer.data)

def multiobj(request):
    data = Person.objects.get(id=1)
    serilaizer = PersonSerializer(data,many=True)
    print(serilaizer.data)