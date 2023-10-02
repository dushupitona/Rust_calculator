from django.shortcuts import render
from calc_page.forms import Raid_form
from calc_page.models import Raid_tool, Raid_object, Resource
from calc_page.res_sort import sort


def index(request):
    if request.method == 'POST':
        form = Raid_form(request.POST)
        if form.is_valid():
            tool = Raid_tool.objects.get(tool_name=form.cleaned_data.get('tool'))
            obj = Raid_object.objects.get(obj_name=form.cleaned_data.get('objct'))
            quan = form.cleaned_data.get('quantity')

            craft_quan = obj.obj_raid.get(tool.tool_val) * quan  #сколько шт скрафтить

            output_dict = tuple({
                        'name': key,
                        'values': '{:,}'.format(value * craft_quan * quan).replace(',', '.'),
                        'img_src': 'media/' + str(Resource.objects.get(res_val=key).res_img)
                                } for key, value in sort(tool.tool_res))  # словарь с данными для вывода

            context = {
                'form': form,
                'bar_img': 'media/' + str(tool.tool_img),
                'out_data': output_dict,
                'quantity': craft_quan
            }

    else:
        context = {
            'form': Raid_form,
        }
    return render(request, 'calc_page/index.html', context=context)