"""karaokelist URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin

from karaoke import views

# la majoria de les views estan fetes amb "generic display views"
# https://docs.djangoproject.com/en/1.10/topics/class-based-views/
# https://docs.djangoproject.com/en/1.10/ref/class-based-views/generic-display/
# https://docs.djangoproject.com/en/1.10/ref/class-based-views/generic-editing/

urlpatterns = [
	url(r'^$', views.ItemListView.as_view() ),
	url(r'^torn$', views.ItemCreateView.as_view(success_url="/list") ),
	url(r'^list$', views.ItemListView.as_view() ),
	url(r'^vota$', views.VotaView.as_view() ),
	url(r'^vota2/(?P<votacio>[0-9])', views.votaActionView ), # view feta amb "metode classic"
    url(r'^admin/', admin.site.urls ),     # view del sistema d'administracio automatic de Django
]
