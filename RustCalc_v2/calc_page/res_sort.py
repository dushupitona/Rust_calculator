from calc_page.models import Resource


def sort(res_dict):  #res_dict - словарь с необходимыми рессурсами для 1 шт
    res_list = [{key: value, 'sort_id': Resource.objects.get(res_val=key).res_sort_id} for key, value in res_dict.items()]
    sorted_list = sorted(res_list, key=lambda x: x['sort_id'])
    [dct.pop('sort_id') for dct in sorted_list]

    out_dict = dict()
    for dct in sorted_list:
        for key, value in dct.items():
            out_dict[key] = value

    return out_dict.items()


