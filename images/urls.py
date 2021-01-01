from django.urls import path

from . import views

urlpatterns = [
    path('upload/', views.ImageUpoadView.as_view(), name='upload'),
]
