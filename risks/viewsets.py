# coding=utf-8

from rest_framework import viewsets, generics
from .serializers import RiskTypesSerializer, PolicyListSerializer, FieldsSerializer
from .models import RiskTypeList, FieldTypes, Fields, PolicyList
from rest_framework.response import Response
import datetime


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
    counter = 0

    def list(self, request):
        queryset = PolicyList.objects.all()
        serializer = PolicyListSerializer(queryset, many=True)
        # print(serializer.data)
        if request.method == 'POST':
            print(' request.data %s ' % request.data)

        return Response(serializer.data)

    def create(self, request):
        if not request.POST._mutable:
            request.POST._mutable = True
        data = request.data
        self.counter += 1

        qs_name = RiskTypeList.objects.filter(id=data['risk_type_id'])

        name = qs_name.values_list('name')[0][0]
        date_now = datetime.datetime.now().date().isoformat()

        data['date'] = date_now
        data['name'] = name[:3].upper() + str(self.counter) + date_now

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    # def create(self, validated_data):
    #     obj = OriginalModel.objects.create(**validated_data)
    #     obj.save(foo=validated_data['foo'])
    #     return obj

    # def retrieve(self, request, pk=None):
    #     print(request)
    #     print('---pk %s' % pk)
    #     # queryset = PolicyList.objects.filter()
