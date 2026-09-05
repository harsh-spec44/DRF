from django.urls import path
from . import views
urlpatterns = [
    path('', views.RootAPIView.as_view(), name='root'),
    path('todo/',views.TodoListCreateView.as_view(), name='list'), # .as_view() :- Used when class based API View
    path('todo/<int:pk>/', views.RetrieveUpdateDestroyAPIView.as_view()),
]
