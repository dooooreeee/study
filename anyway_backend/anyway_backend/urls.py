from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from addresses import views


urlpatterns = [
    path('login/',views.login),
    path('addresses/<int:pk>/',views.address),
    path('addresses/',views.addresses_list),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]