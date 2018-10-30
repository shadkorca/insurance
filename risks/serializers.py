# coding=utf-8

from rest_framework import serializers
# from .models import RiskTypeModel
from .models import RiskTypeList, FieldTypes, Fields, PolicyList




class FieldsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fields
        fields = '__all__'


class RiskTypesSerializer(serializers.ModelSerializer):
    # fields = FieldsSerializer(many=True)

    class Meta:
        model = RiskTypeList
        fields = '__all__'


class PolicyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = PolicyList
        fields = '__all__'



