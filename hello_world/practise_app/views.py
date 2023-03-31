from django.shortcuts import render
from .models import MYTEST

def test(request):
    if request.method =='POST':
        m=MYTEST()
        m.na=request.POST['na']
        m.num=request.POST.get('num')
        m.pwd=request.POST.get('pwd')
        m.save()
    return render(request,'practise.html')
    # else:
    #     return HttpResponse("learnsomething")

# Create your views here.
