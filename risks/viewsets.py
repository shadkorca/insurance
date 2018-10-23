# coding=utf-8

from rest_framework import viewsets
# from .serializers import RiskSerializer
from .serializers import FieldTypesSerializer
# from .models import RiskTypeModel
from .models import RiskTypeList, FieldTypes, Fields, PolicyList


# class RiskViewSet(viewsets.ModelViewSet):
#     queryset = RiskTypeModel.objects.all().order_by('-created_at')
#     serializer_class = RiskSerializer

class RiskViewSet(viewsets.ModelViewSet):
    types_list = ['Number', 'Text', 'Checkbox', 'Date']
    # for type in types_list:
        # FieldTypes.objects.get_or_create(type_name=type)
    a = FieldTypes.objects.filter(type_name__in=types_list)
    if not a:
        for type in types_list:
            FieldTypes.objects.create(type_name=type)
    # a = FieldTypes.objects.all().values_list('type_name')

    # queryset = Fields.objects.all()
    queryset = RiskTypeList.objects.all()
    serializer_class = FieldTypesSerializer
