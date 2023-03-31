from django.shortcuts import render
from .models import adding

def post(request):  #---->post,create
    if request.method == 'POST':
        a = adding()
        a.number_1 = request.POST['number_1']
        a.number_2 = request.POST['number_2']
        a.save()
    return render(request, 'adding.html')

def get(request):    #------>read,get
    a=adding.objects.all()
    return render(request,"result.html",{"adding":a})

def delt(request, id): #------->delete
    a=adding.objects.get(id=id)
    a.delete()
    return  render(request,'result.html')


def reload(request,id):  #------->upload
    a=adding.objects.get(id=id)
    if request.method == "POST":
        a.number_1 = request.POST.get('number_1')
        a.number_2 = request.POST.get('number_2')
        a.save()
    return render(request,'update.html',{'adding':a})
