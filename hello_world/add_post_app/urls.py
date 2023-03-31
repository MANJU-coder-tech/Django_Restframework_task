from django.urls import path
from .import views

urlpatterns=[
    path('add/',views.post, name='post'),
    path("read",views.get,name="get"),
    path('delete/<int:id>/',views.delt, name=""),
    path('update/<int:id>/',views.reload,name="reload")

]