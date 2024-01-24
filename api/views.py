from rest_framework.generics import ListAPIView

from calc_page.models import Raid_object
from calc_page.serializers import Raid_object_serializer


class Raid_object_ListAPIView(ListAPIView):
    queryset = Raid_object.objects.all()
    serializer_class = Raid_object_serializer
