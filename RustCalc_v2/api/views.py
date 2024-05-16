from rest_framework.views import APIView
from api.serializers import ToolsSerializer, ObjectsSerializer, CalculateSerializer
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from calc_page.models import Raid_tool, Raid_object, Resource
from calc_page.res_sort import sort

# Create your views here.


class ToolsAPIView(ListAPIView):
    serializer_class = ToolsSerializer
    queryset = Raid_tool.objects.all()


class ObjectsAPIView(ListAPIView):
    serializer_class = ObjectsSerializer
    queryset = Raid_object.objects.all()


class CalculateApiView(APIView):

    def post(self, request):
        serializer = CalculateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                tool = Raid_tool.objects.get(id=serializer.validated_data['tool_id'])
                obj = Raid_object.objects.get(id=serializer.validated_data['obj_id'])
                quan = serializer.validated_data['value']

                craft_quan = obj.obj_raid.get(tool.tool_val) * quan

                output_dict = tuple(
                    {
                        'name': key,
                        'values': '{:,}'.format(value * craft_quan).replace(',', '.'),
                    } for key, value in sort(tool.tool_res))

                return Response({'tool': tool.tool_name, 'quantity': craft_quan, 'resources': output_dict})
            except:
                return Response('Invalid data', status=400)
        else:
            return Response(serializer.errors, status=400)

