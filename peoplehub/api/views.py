from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from  rest_framework import status

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
        serilaizer = PersonSerializer(data = parsed_data)
        if serilaizer.is_valid():
            serilaizer.save()
            return JsonResponse({"create":"successfull"}, status=status.HTTP_201_CREATED)

        return JsonResponse(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    data = Person.objects.all()
    serilaizer = PersonSerializer(data,many=True)
    json_data = JSONRenderer().render(serilaizer.data)
    return HttpResponse(json_data, 
                        content_type='application/json')