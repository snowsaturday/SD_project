from django.shortcuts import render
from .models import licenses
from services.models import service_group
from contacts.models import contact


def index_view(request):
    context = {
        "licenses": licenses.objects.all(),
        "groups": service_group.objects.all(),
        "contacts": contact.objects.all(),
    }

    return render(request, 'index.html', context)