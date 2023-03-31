from django.urls import path
from .import views

urlpatterns = [
    path('form/',views.employee_form, name='employee'),
    path('list/',views.employee_list,name='employee_read'),
    path('delete/<int:id>/',views.employee_delete),
    path('delete/<int:phone_no>/',views.employee_delete)
    ]