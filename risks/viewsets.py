# coding=utf-8

from .serializers import RiskTypesSerializer, PolicyListSerializer, FieldsSerializer
from .models import RiskTypeList, FieldTypes, Fields, PolicyList
from rest_framework.response import Response
from rest_framework import mixins, status, viewsets
import datetime


# class RiskViewSet(mixins.CreateModelMixin,
#                   mixins.DestroyModelMixin,
#                   mixins.ListModelMixin,
#                   viewsets.GenericViewSet):
class RiskViewSet(viewsets.ModelViewSet):
    types_list = ['Number', 'Text', 'Checkbox', 'Date']
    # for type in types_list:
    # a = FieldTypes.objects.filter(type_name__in=types_list)
    # if not a:
    #     for type in types_list:
    #         FieldTypes.objects.create(type_name=type)
    queryset = RiskTypeList.objects.all()
    serializer_class = RiskTypesSerializer

    # def retrieve(self, request, pk=None):
    #     queryset = Fields.objects.filter(risk_type_id=pk)
    #     serializer = FieldsSerializer(queryset, many=True)
    #     return Response(serializer.data)

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


class RiskFieldsView(viewsets.ModelViewSet):
    queryset = Fields.objects.all()
    serializer_class = FieldsSerializer
    # http_method_names = ['get', 'post', 'head', 'option']

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
        # serializer = FieldsSerializer(queryset, many=True)
        super().perform_destroy(queryset)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PolicyViewSets(viewsets.ModelViewSet):
    queryset = PolicyList.objects.all()
    serializer_class = PolicyListSerializer

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

        qs_name = RiskTypeList.objects.filter(id=data['risk_type_id'])

        name = qs_name.values_list('name')[0][0]
        date_now = datetime.datetime.now()

        data['date'] = date_now.date().isoformat()
        data['name'] = '%s-%s%s%s%s' % (name[:3].upper(), date_now.second, date_now.minute, date_now.hour, date_now.day)
        # data['name'] = name[:3].upper() + str(self.counter) + date_now

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


    # def retrieve(self, request, pk=None):
    #     print(request)
    #     print('---pk %s' % pk)
    #     # queryset = PolicyList.objects.filter()
