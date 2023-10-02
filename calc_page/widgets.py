from django import forms
from calc_page.models import Raid_tool, Raid_object


class CustomSelectTool(forms.widgets.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super(CustomSelectTool, self).create_option(name, value, label, selected, index, subindex, attrs)
        qry = Raid_tool.objects.get(tool_name=option['label'])
        img_src = 'media/' + str(qry.tool_img)
        option['attrs']['data-img_src'] = img_src
        return option


class CustomSelectObj(forms.widgets.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super(CustomSelectObj, self).create_option(name, value, label, selected, index, subindex, attrs)
        qry = Raid_object.objects.get(obj_name=option['label'])
        img_src = 'media/' + str(qry.obj_img)
        option['attrs']['data-img_src'] = img_src
        return option
