from django.contrib import admin
from django.urls import path

from api.views import ToolsAPIView, ObjectsAPIView, CalculateApiView



app_name = 'api'

urlpatterns = [
    path('tools/', ToolsAPIView.as_view()),
    path('objects/', ObjectsAPIView.as_view()),
    path('calculate/', CalculateApiView.as_view()),
]