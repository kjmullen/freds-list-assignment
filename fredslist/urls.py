"""fredslist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from classifieds.views import IndexView, SessionCity
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse_lazy
from userprofiles.views import RegisterUser
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'cities/redirect/(?P<pk>\d+)/$', SessionCity.as_view(),
        name="redirect_city"),
    url(r'^api/', include("api.urls")),
    url(r'^u/', include("userprofiles.urls")),
    url(r'^l/', include("classifieds.urls")),
    url(r'^logout/$', logout, {'next_page': reverse_lazy('index')},
        name='logout'),
    url(r'^register/$', RegisterUser.as_view(), name="register"),
    url('^', include('django.contrib.auth.urls')),
    url('^$', IndexView.as_view(), name="index"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
