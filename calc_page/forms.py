from calc_page.models import Raid_tool, Raid_object, Resource


from django import forms
from . import widgets as CustomWidget


class Raid_form(forms.Form):
    tool = forms.ModelChoiceField(
            empty_label=None,
            label='',
            initial=None,
            queryset=Raid_tool.objects.order_by('tool_drop_id'),
            widget=CustomWidget.CustomSelectTool(
            attrs={'id': 'id_select_1',        # id для select
                   'style': 'width: 350px; '})
    )

    objct = forms.ModelChoiceField(
            empty_label=None,
            label='',
            initial=None,
            queryset=Raid_object.objects.order_by('obj_drop_id'),
            widget=CustomWidget.CustomSelectObj(
            attrs={'id': 'id_select_2',         # id для select
                   'style': 'width: 350px; '})
    )

    quantity = forms.IntegerField(min_value=1, max_value=50, initial=1, widget=forms.NumberInput(
        attrs={
            'class': 'vol_input'
        }
    ))