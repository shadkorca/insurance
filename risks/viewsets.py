# coding=utf-8

from .serializers import RiskTypesSerializer, PolicyListSerializer, FieldsSerializer, PolicyFieldsSerializer
from .models import RiskTypeList, FieldTypes, Fields, PolicyList, FieldValue
from rest_framework.response import Response
from rest_framework import status, viewsets
import datetime


class RiskViewSet(viewsets.ModelViewSet):
    types_list = ['Number', 'Text', 'Checkbox', 'Date']
    a = FieldTypes.objects.filter(type_name__in=types_list)
    if not a:
        for type in types_list:
            FieldTypes.objects.create(type_name=type)
    queryset = RiskTypeList.objects.all()
    serializer_class = RiskTypesSerializer


class RiskFieldsView(viewsets.ModelViewSet):
    queryset = Fields.objects.all()
    serializer_class = FieldsSerializer

    def list(self, request, pk=None, sk=None):
        if not sk:
            queryset = Fields.objects.filter(risk_type_id=pk)
            serializer = FieldsSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            queryset = Fields.objects.filter(risk_type_id=pk).filter(id=sk)
            serializer = FieldsSerializer(queryset, many=True)
            return Response(serializer.data)

    def destroy(self, request, pk=None, sk=None):
        queryset = Fields.objects.filter(risk_type_id=pk).filter(id=sk)
        super().perform_destroy(queryset)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PolicyViewSets(viewsets.ModelViewSet):
    queryset = PolicyList.objects.all()
    serializer_class = PolicyListSerializer

    def create(self, request):
        if not request.POST._mutable:
            request.POST._mutable = True
        data = request.data

        qs_name = RiskTypeList.objects.filter(id=data['risk_type_id'])

        name = qs_name.values_list('name')[0][0]
        date_now = datetime.datetime.now()

        data['date'] = date_now.date().isoformat()
        data['name'] = '%s-%s%s%s%s' % (name[:3].upper(), date_now.second, date_now.minute, date_now.hour, date_now.day)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            field_qs = Fields.objects.filter(risk_type_id=serializer.data['risk_type_id'])
            policie_qs = PolicyList.objects.get(id=serializer.data['id'])
            for i in field_qs:
                FieldValue.objects.get_or_create(field_type=i, policie_id=policie_qs)

        return Response(serializer.data)


class PolicyFieldsView(viewsets.ModelViewSet):
    queryset = FieldValue.objects.all()
    serializer_class = PolicyFieldsSerializer

    def list(self, request, pk=None, sk=None):
        if not sk:
            queryset = FieldValue.objects.filter(policie_id=pk)
            serializer = PolicyFieldsSerializer(queryset, many=True)
            return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.queryset.get(id=kwargs.get('sk'))
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
