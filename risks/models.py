from django.db import models
from django.contrib.contenttypes.models import ContentType


class FieldTypes(models.Model):
    # названия имеющихся типов поля, те текстовый и тд
    type_name = models.CharField(max_length=60)

    def __str__(self):
        return self.type_name


class RiskTypeList(models.Model):
    # название типа риска, машина, дом и тд
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Fields(models.Model):
    # названия полей и к какому риску относиться
    field_name = models.CharField(max_length=60)
    risk_type_id = models.ForeignKey(RiskTypeList, related_name='fields', on_delete=models.CASCADE)
    field_type_id = models.ForeignKey(FieldTypes, on_delete=models.CASCADE)
    enumerate = models.BooleanField()
    enum_text = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.field_name


class PolicyList(models.Model):
    name = models.CharField(max_length=60)
    risk_type_id = models.ForeignKey(RiskTypeList, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.name


class FieldValue(models.Model):
    field_type = models.ForeignKey(Fields, on_delete=models.CASCADE)
    field_value = models.CharField(max_length=80)

    def __str__(self):
        return '%s %s' % (self.field_type.field_name,  self.field_value)
