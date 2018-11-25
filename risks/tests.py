from django.test import TestCase

from rest_framework.test import APIClient
from .models import FieldTypes, RiskTypeList, Fields, PolicyList


class ModelCase(TestCase):
    client = APIClient()

    def setUp(self):
        self.field_type = FieldTypes.objects.create(type_name='Number')
        self.risk_type = RiskTypeList.objects.create(name='Phone')

        self.fields = Fields.objects.create(
            field_name='Price',
            enumerate=False,
            enum_text='',
            risk_type_id=self.risk_type,
            field_type_id=self.field_type
        )

        self.policy = PolicyList.objects.create(
            name='IPH-112233',
            risk_type_id = self.risk_type,
            date='2018-11-22'
        )

        count_field_type = FieldTypes.objects.count()
        count_risk = RiskTypeList.objects.count()
        count_policy = PolicyList.objects.count()
        count_fields = Fields.objects.count()

        self.assertEqual(count_field_type, 5)
        self.assertEqual(count_risk, 1)
        self.assertEqual(count_fields, 1)
        self.assertEqual(count_policy, 1)

    def testGetRequest(self):
        request_risks_client = self.client.get('/api/risks/')
        request_policies_client = self.client.get('/api/policies/')

        self.assertEqual(request_risks_client.status_code, 200)
        self.assertEqual(request_policies_client.status_code, 200)
