# coding=utf-8

from rest_framework import serializers
# from .models import RiskTypeModel
from .models import RiskTypeList, FieldTypes, Fields, PolicyList


class FieldTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = RiskTypeList
        fields = '__all__'

