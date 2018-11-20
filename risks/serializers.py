# coding=utf-8

from rest_framework import serializers
from .models import RiskTypeList, Fields, PolicyList, FieldValue


class FieldsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fields
        fields = '__all__'


class RiskTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = RiskTypeList
        fields = '__all__'


class PolicyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = PolicyList
        fields = '__all__'


class PolicyFieldsSerializer(serializers.ModelSerializer):
    field_type = FieldsSerializer()

    class Meta:
        model = FieldValue
        fields = '__all__'
