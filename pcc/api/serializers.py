from pyrsistent import field
from rest_framework import routers,serializers,viewsets
from . import models

class MilitantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Militant
        fields = [
            'Sex', 'Status', 'ci', 'militant_name', 'first_lastname', 'second_lastname', 
            'register_date', 'militant_core', 'militant_address', 'declaration_date'
        ]