from rest_framework import serializers, validators

from calc_page.models import Raid_tool, Raid_object

class ToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raid_tool
        fields = ['id', 'tool_name']


class ObjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raid_object
        fields = ['id', 'obj_name']


class CalculateSerializer(serializers.Serializer):
        obj_id = serializers.IntegerField(min_value=1, max_value=50)
        tool_id = serializers.IntegerField(min_value=1, max_value=50)
        value = serializers.IntegerField(min_value=1, max_value=50)