from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer, PersonModelSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from  rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin,DestroyModelMixin,UpdateModelMixin,ListModelMixin,RetrieveModelMixin
# Create your views here.

@api_view(['GET','PUT','PATCH'])
def singleobj(request, id):
    
    data = get_object_or_404(Person,id=id)

    if request.method == "PUT":
        parsed_data = request.data
        serilaizer = PersonModelSerializer(data,data=parsed_data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response({'update':'success'})
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PATCH":
         parsed_data = request.data
         serilaizer = PersonModelSerializer(data,data=parsed_data, partial=True)
         if serilaizer.is_valid():
            serilaizer.save()
            return Response({'update':'success'})
         return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    if request.method == 'GET':

     serilaizer = PersonModelSerializer(data)
     return Response(serilaizer.data)

@api_view(['GET','POST'])
def multiobj(request):

    if request.method == "POST":
        parsed_data = request.data
        serilaizer = PersonModelSerializer(data = parsed_data)
        serilaizer.is_valid(raise_exception=True)
        serilaizer.save()
        return Response({"create":"successfull"}, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
     print(request.accepted_renderer)
     data = Person.objects.all()
     serilaizer = PersonModelSerializer(data,many=True)
     return Response(serilaizer.data)

class MultipleObjAPIView(CreateModelMixin,ListModelMixin, GenericAPIView):
   queryset = Person.objects.all()
   serializer_class = PersonModelSerializer

# args-unnamed parameters as pupil
# kwargs-named parameters as dictionary
   def get(self, request,*args, **kwargs):
     return self.list(request, *args, **kwargs,)
   
   def post(self, request):

     return self.create(request)

class SingleObjAPIView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    def get(self, request,*args, **kwargs):
        
        return self.retrieve(request,*args, **kwargs)
    
    def put(self, request, *args, **kwargs):
 
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):

        return self.partial_update(request, *args, **kwargs)

    def delete(self, request,*args, **kwargs):
       
       return self.destroy(request, *args, **kwargs)
 

