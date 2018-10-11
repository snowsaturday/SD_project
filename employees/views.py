from django.shortcuts import render
from employees.models import employe

def emlpoyees_list_view(request):

    context = {
        "employees": employe.objects.all(),
               }

    return render(request, 'employees_list.html', context)


def emlpoye_detail(request, pk=0):

    context = {
        "employe": employe.objects.get(pk=pk),
               }

    return render(request, 'employe_detail.html', context)