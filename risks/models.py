from django.db import models
from django.contrib.contenttypes.models import ContentType


class FieldTypes(models.Model):
    # name of existed type of field such as text, number etc.
    type_name = models.CharField(max_length=60)

    def __str__(self):
        return self.type_name


class RiskTypeList(models.Model):
    # name of risk type such as car or house
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Fields(models.Model):
    # name of fields and what risks refer
    field_name = models.CharField(max_length=60)
    risk_type_id = models.ForeignKey(RiskTypeList, related_name='fields', on_delete=models.CASCADE)
    field_type_id = models.ForeignKey(FieldTypes, on_delete=models.CASCADE)
    enumerate = models.BooleanField()
    enum_text = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.field_name


class PolicyList(models.Model):
    # list of policies
    name = models.CharField(max_length=60)
    risk_type_id = models.ForeignKey(RiskTypeList, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.name
