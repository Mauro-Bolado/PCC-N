from pyexpat import model
from attr import fields
from matplotlib.pyplot import cla
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

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Address
        fields = [
            'street', 'municipality', 'province', 'neighborhood', 'corner_or_ave', 'apto'
        ]

class CoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Core
        fields = [
            'code', 'core_name', 'district', 'political_area', 'sector', 'subordinate'
        ]

class DeclarationDateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.DeclarationDate
        fields = [
            'declaration_date'
        ]

class PaymentDateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PaymentDate
        fields = [
            'payment_date'
        ]

class PaymentNormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PaymentNorm
        fields = [
            'lower_limit', 'upper_limit', 'percent', 'amount_to_pay'
        ]

class PaymentDeclarationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PaymentDeclaration
        fields = [
            'salary', 'year', 'month', 'payment_norm', 'share', 
            'declaration_date', 'payment_militant', 'payment_date'
        ]

class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Payment
        fields = [
            'payment_declaration', 'payment_date', 'amount'
        ]

class TaskSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Task
        fields = [
            'task_name', 'orientation', 'militants'
        ]

class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    model = models.Participant
    fields = [
        'task_militant', 'participant_task', 'evaluator', 'evaluation'
    ]