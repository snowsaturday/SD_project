from django.shortcuts import render
from .models import service_group, service


def services_main_view(request):
    context = {
        "items": service.objects.all().filter(group__is_main=True).order_by('name'),
        "groups": service_group.objects.all().order_by('name')
    }
    return render(request, 'services.html', context)


def services_group_item_view(request, group_id=0):
    context = {
        "items": service.objects.all().filter(group_id=group_id).order_by('name'),
        "items_add_to_cat": service.objects.all().filter(add_to_group=group_id),
        "group": service_group.objects.get(id=group_id),
        "groups": service_group.objects.all().order_by('name'),
        "active_group": group_id,
    }
    return render(request, 'services_group_item_list.html', context)


def services_detail_item_view(request, group_id=0, item_id=0):
    context = {
        "item": service.objects.get(id=item_id),
        "groups": service_group.objects.all().order_by('name'),
        "group": service_group.objects.get(id=group_id),
    }
    return render(request, 'services_item_detail.html', context)
