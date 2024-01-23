from django.contrib import admin
from django.urls import path

from api.views import Raid_object_ListAPIView

app_name = 'api'

urlpatterns = [
    path('raid-object-list/',Raid_object_ListAPIView.as_view(), name='object_list'),
]
