from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def singleobj(request):
    data = Person.objects.get(id=1)
    serilaizer = PersonSerializer(data)
    json_data = JSONRenderer().render(serilaizer.data)
    return HttpResponse(json_data, 
                        content_type='application/json')

@csrf_exempt
def multiobj(request):
    if request.method == "POST":
        json = request.body
        stream = io.BytesIO(json)
        parsed_data = JSONParser().parse(stream)
        print(parsed_data)
    data = Person.objects.all()
    serilaizer = PersonSerializer(data,many=True)
    json_data = JSONRenderer().render(serilaizer.data)
    return HttpResponse(json_data, 
                        content_type='application/json')