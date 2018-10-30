# coding=utf-8

from rest_framework import viewsets, generics
from .serializers import RiskTypesSerializer, PolicyListSerializer, FieldsSerializer
from .models import RiskTypeList, FieldTypes, Fields, PolicyList
from rest_framework.response import Response


# class RiskViewSet(viewsets.ViewSet):
class RiskViewSet(viewsets.ModelViewSet):
    types_list = ['Number', 'Text', 'Checkbox', 'Date']
    # for type in types_list:
    a = FieldTypes.objects.filter(type_name__in=types_list)
    if not a:
        for type in types_list:
            FieldTypes.objects.create(type_name=type)
    queryset = RiskTypeList.objects.all()
    serializer_class = RiskTypesSerializer

    def list(self, request):
        queryset = RiskTypeList.objects.all()
        serializer = RiskTypesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Fields.objects.filter(risk_type_id=pk)
        serializer = FieldsSerializer(queryset, many=True)
        return Response(serializer.data)

    # def update(self, request, pk=None):
    #     queryset = Fields.objects.filter(risk_type_id=pk)
    #     serializer = FieldsSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def destroy(self, request, pk=None):
    #     queryset = Fields.objects.filter(risk_type_id=pk)
    #     serializer = FieldsSerializer(queryset, many=True)
    #     print('pk %s' % pk)
    #     print('request %s' % format(request))
    #     return Response(serializer.data)


class PolicyViewSets(viewsets.ModelViewSet):
    queryset = PolicyList.objects.all()
    serializer_class = PolicyListSerializer
