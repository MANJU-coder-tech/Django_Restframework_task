from django.shortcuts import render
from .models import Employee

def employee_list(request):#read--->display list of employee
    ee = Employee.objects.all()
    return render(request,'employee_list.html',{"Employee":ee})

def employee_form(request): #get,post ---->insert,update
    if request.method == 'POST':
        e = Employee()
        e.user_name = request.POST.get('user_name')

        e.email_id = request.POST.get('email_id')
        e.phone_no = request.POST.get('phone_no')
        e.address = request.POST.get('address')
        e.save()

    return render(request, 'employee_form.html')


def employee_delete(request, id,phone_no):
    dd=Employee.objects.get(id=id)
    dd=Employee.objects.get(phone_no=phone_no)
    dd.delete()
    return render(request,'employee_list.html')
