from django.urls import path
from .views import cre,read
urlpatterns = [
    path('post', cre.as_view() ),
    path('read',read.as_view() )



]
