# coding=utf-8

from rest_framework import serializers
from .models import RiskTypeModel


class RiskSerializer(serializers.ModelSerializer):

    class Meta:
        model = RiskTypeModel
        fields = '__all__'

