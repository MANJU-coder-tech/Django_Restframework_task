from rest_framework import serializers

from .models import Snip_db


class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = Snip_db
        fields = ["name","ticket_no","source","destination","price"]