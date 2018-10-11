from django.shortcuts import render
from .models import invitro_group, invitro_items, invitro_profile


def main_view(request):

    context = {
        "profiles": invitro_profile.objects.all()
    }

    return render(request, 'analyzes.html', context)


def groups_list_view(request, p_id=0):

    context = {"items": invitro_items.objects.all().filter(group__profile__slug_id=p_id),
               "groups": invitro_group.objects.all().filter(profile__slug_id=p_id),
               "profiles": invitro_profile.objects.all(),
               "profile": invitro_profile.objects.all().filter(slug_id=p_id),
               "pid": p_id
               }

    return render(request, 'analyzes_groups_list.html', context)


def group_list_view(request, p_id=0, g_id=0):

    context = {"items": invitro_items.objects.all().filter(group__slug_id=g_id),
               "groups": invitro_group.objects.all().filter(slug_id=g_id),
               "profiles": invitro_profile.objects.all(),
               "profile": invitro_profile.objects.all().filter(slug_id=p_id),
               "pid": p_id,
               "gid": g_id
               }

    return render(request, 'analyzes_group.html', context)


def detail_view(request, p_id=0, g_id=0, item_id=0):

    context = {"items": invitro_items.objects.all().filter(slug_id=item_id),
               "groups": invitro_group.objects.all().filter(slug_id=g_id),
               "profiles": invitro_profile.objects.all(),
               "profile": invitro_profile.objects.all().filter(slug_id=p_id),
               "pid": p_id,
               "gid": g_id,
               "iid": item_id
               }

    return render(request, 'analyzes_detail.html', context)
