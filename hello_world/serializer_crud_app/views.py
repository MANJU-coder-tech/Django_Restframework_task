from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Snip_db
from .serializer import Postserializer
from django.http import HttpResponse,JsonResponse


class cre(generics.GenericAPIView):
    serializer_class=Postserializer

    def post(self,request):
        p = Postserializer(data=request.data)
        p.name=request.data['name']
        p.ticket_no = request.data['ticket_no']
        p.source = request.data['source']
        p.destination = request.data['destination']
        p.price = request.data['price']
        p.is_valid()
        p.save()
        return Response(Postserializer(p).data)
    # Create your views here.

class read(generics.ListAPIView):
    queryset = Snip_db.objects.all()
    serializer_class = Postserializer




