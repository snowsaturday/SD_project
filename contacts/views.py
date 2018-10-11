from django.shortcuts import render
from .models import contact

# Create your views here.

def contacts_view(request):

    context = {
        "contacts": contact.objects.all()
    }

    return render(request, 'contacts.html', context)
