from django.shortcuts import render,HttpResponse,redirect
from .models import Signin

def signin(request):
    if request.method=='POST':

        uname = request.POST['user_name']
        password = request.POST['password']
        user =  Signin.objects.get(user_name=uname)
        if  password==user.password:
            return HttpResponse("successfully signin")

    return render(request,'sign_in.html')


def signup(request):
    if request.method == 'POST':
        e = Signin()
        e.user_name = request.POST.get('user_name')
        e.email_id = request.POST.get('email_id')
        e.phone_no = request.POST.get('phone_no')
        e.address = request.POST.get('address')
        e.password=request.POST.get('password')

        e.save()
            #return HttpResponse("account created successfully")
    return render(request,'sign_up.html')





