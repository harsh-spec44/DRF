from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from  rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.

@csrf_exempt
def singleobj(request):
    
    data = get_object_or_404(Person, id=id)

    if request.method == "PUT":
        stream = io.BytesIO(request.body)
        parsed_data = JSONParser().parse(stream)
        serilaizer = PersonSerializer(data,data=parsed_data)
        if serilaizer.is_valid():
            serilaizer.save()
            return JsonResponse({'update':'success'})
        return JsonResponse(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PATCH":
        stream = io.BytesIO(request.body)
        parsed_data = JSONParser().parse(stream)
        serilaizer = PersonSerializer(data,data=parsed_data, partial=True)
        if serilaizer.is_valid():
            serilaizer.save()
            return JsonResponse({'update':'success'})
        return JsonResponse(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

    serilaizer = PersonSerializer(data)
    return JsonResponse(serilaizer.data)

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
    return JsonResponse(serilaizer.data, safe=False)