from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class RiskTypeModel(models.Model):
    type_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(auto_created=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.type_name


class NumberModel(models.Model):
    numb = models.IntegerField()
    content = GenericRelation(RiskTypeModel)

    def __str__(self):
        return 'Number'


class DateModel(models.Model):
    risk_date = models.DateTimeField(auto_now_add=True)
    content = GenericRelation(RiskTypeModel)

    def __str__(self):
        return 'Date'


class TextModel(models.Model):
    field_name = models.CharField(max_length=255)
    content = GenericRelation(RiskTypeModel)

    def __str__(self):
        return 'Text'

class CheckModel(models.Model):
    checked = models.BooleanField()
    content = GenericRelation(RiskTypeModel)

    def __str__(self):
        return 'Checkbox'

