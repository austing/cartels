from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^invitation/', include('invitations.urls', namespace='invitations')),
    url(r'^', include('problems.urls', namespace='problems')),
]
