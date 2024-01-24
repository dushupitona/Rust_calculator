from rest_framework import serializers

from calc_page.models import Raid_object


class Raid_object_serializer(serializers.ModelSerializer):
    class Meta:
        model = Raid_object
        fields = ('id', 'obj_name', 'obj_val', 'obj_img' ,'obj_raid')