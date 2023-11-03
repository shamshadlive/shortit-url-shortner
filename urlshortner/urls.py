from django.urls import path, include
from .import views



urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<str:pk>/", views.go_to_url, name="go_to_url"),
    
    ]
