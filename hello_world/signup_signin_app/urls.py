from django.urls import path
from.views import*
urlpatterns = [

    path('lgup',signup),
    path('lgin',signin)
]
