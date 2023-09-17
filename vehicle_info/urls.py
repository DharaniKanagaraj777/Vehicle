from django.urls import path

from . import views

urlpatterns=[
    path('',views.home),
    path('car',views.car),
    path('bike',views.bike),
    path('hello',views.hello),
    path('hello1',views.hello1),
    path('hello2',views.hello2),
    path('evenodd',views.evenodd)
]