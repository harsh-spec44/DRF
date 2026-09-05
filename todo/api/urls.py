from django.urls import path
from . import views
urlpatterns = [
    path('todo/',views.TodoListCreateView.as_view()), # .as_view() :- Used when class based API View
    path('todo/<int:pk>/', views.RetrieveUpdateDestroyAPIView.as_view()),
]
