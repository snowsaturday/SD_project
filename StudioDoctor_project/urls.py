"""StudioDoctor_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from main.views import index_view
from invitro_data.views import main_view, groups_list_view, group_list_view, detail_view
from employees.views import emlpoyees_list_view, emlpoye_detail
from services.views import services_main_view, services_group_item_view, services_detail_item_view
from contacts.views import contacts_view

urlpatterns = [
    url(r'^$', index_view),
    url(r'^admin/', admin.site.urls),
    url(r'^analyzes/$', main_view, name='analyzes'),
    url(r'^analyzes/(?P<p_id>\d+)/$', groups_list_view),
    url(r'^analyzes/(?P<p_id>\d+)/(?P<g_id>\d+)/$', group_list_view),
    url(r'^analyzes/(?P<p_id>\d+)/(?P<g_id>\d+)/(?P<item_id>\d+)/', detail_view),
    url(r'^employees/$', emlpoyees_list_view),
    url(r'^employees/(?P<pk>\d+)/', emlpoye_detail),
    url(r'^services/$', services_main_view),
    url(r'^services/(?P<group_id>\d+)/$', services_group_item_view),
    url(r'^services/(?P<group_id>\d+)/(?P<item_id>\d+)/$', services_detail_item_view),
    #url(r'^contacts/$', contacts_view),
]

# Эта строка опциональна и будет добавлять url'ы только при DEBUG = True
if settings.DEBUG:

    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
