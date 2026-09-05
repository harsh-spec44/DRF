from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Todo
from .serializers import TodoSerializer
# Create your views here.
class TodoListCreateView(ListCreateAPIView):
     queryset = Todo.objects.all()
     serializer_class = TodoSerializer

     def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class TodoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
     queryset = Todo.objects.all()
     serializer_class= TodoSerializer