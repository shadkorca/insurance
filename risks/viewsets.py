# coding=utf-8

from rest_framework import viewsets
from .serializers import RiskSerializer
from .models import RiskTypeModel


class RiskViewSet(viewsets.ModelViewSet):
    queryset = RiskTypeModel.objects.all().order_by('-created_at')
    serializer_class = RiskSerializer
