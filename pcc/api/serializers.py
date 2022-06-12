# from rest_framework import routers,serializers,viewsets
# from .models import *

# class MilitantSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Militant
#         fields = '__all__'

# class DebtsSerializer(object):

#     @staticmethod
#     def serialize(militants, many=False):
#         indexs = []

#         for mil in militants:
#             share = mil.arrears_fees()
#             if len(share) > 0:
#                 indexs.append(mil.ci)
        
#         militants_filter = []
#         for item in indexs:
#             militants_filter.append(Militant.objects.get(pk=item))

#         militant_debts = MilitantSerializer(militants_filter, many=True)
#         meta = ['ci', 'militant_name', 'first_lastname', 'second_lastname']

#         index = 0
#         for mil in militants_filter:
#             share = mil.arrears_fees()
            
#             for key in militant_debts.data[index].keys():
#                 if key not in meta:
#                     del militant_debts.data[index][key]

#             militant_debts.data[index]['debts'] = share
#             index += 1

#         if many:
#             return militant_debts
#         return militant_debts.data[0]


# class AddressSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Address
#         fields = '__all__'
        

# class CoreSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Core
#         fields = '__all__'

# class DeclarationDateSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = DeclarationDate
#         fields = ['declaration_date']

# class PaymentDateSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = PaymentDate
#         fields = ['payment_date']

# class PaymentNormSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = PaymentNorm
#         fields = '__all__'

# class PaymentDeclarationSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = PaymentDeclaration
#         fields = '__all__'

# class PaymentSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Payment
#         fields = '__all__'

# class TaskSerilizer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Task
#         fields = '__all__'

# class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Participant
#         fields = '__all__'

from operator import index
from rest_framework import serializers
from django.contrib.auth.models import User, Group

from api.models import Address, PaymentDate, Militant, Core, Payment, PaymentDeclaration, DeclarationDate


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        exclude = ['payment_declaration']


class PaymentDeclarationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDeclaration
        exclude = ['militant']


class DeclarationDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeclarationDate
        fields = "__all__"


class PaymentDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDate
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class MilitantSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Militant
        fields = ['ci', 'militant_name', 'first_lastname',
                  'second_lastname', 'address']


class MilitantDeclarationsSerializer(serializers.ModelSerializer):
    payment_declaration = PaymentDeclarationSerializer(
        many=True, read_only=True)
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Militant
        fields = ['ci', 'militant_name', 'first_lastname',
                  'second_lastname', 'address', 'payment_declaration']


class MilitantDebtsSerializer(object):

    @staticmethod
    def serialize(militants, many=False):
        indexs = []

        for mil in militants:
            share = mil.arrears_fees()
            if len(share) > 0:
                indexs.append(mil.ci)
        
        militants_filter = []
        for item in indexs:
            militants_filter.append(Militant.objects.get(pk=item))

        militant_debts = MilitantSerializer(militants_filter, many=True)

        index = 0
        for mil in militants_filter:
            share = mil.arrears_fees()
            militant_debts.data[index]['debts'] = share
            index += 1

        if many:
            return militant_debts.data
        return militant_debts.data[0]


class CoreSerializer(serializers.ModelSerializer):
    militants = MilitantSerializer(many=True, read_only=True)

    class Meta:
        model = Core
        fields = ['code', 'core_name', 'district', 'political_area',
                  'sector', 'subordinate', 'militants']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['last_login']


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'
