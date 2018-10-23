from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


# Create your models here.
# class RiskTypeModel(models.Model):
#     type_name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField(auto_created=True)
#     content_object = GenericForeignKey('content_type', 'object_id')
#
#     def __str__(self):
#         return self.type_name


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
    risk_type_id = models.ForeignKey(RiskTypeList, on_delete=models.CASCADE)
    field_type_id = models.ForeignKey(FieldTypes, on_delete=models.CASCADE)
    enumerate = models.BooleanField()
    enum_text = models.CharField(max_length=60)

    def __str__(self):
        return self.field_name


class EnumerateVariants(models.Model):
    text = models.CharField(max_length=60)
    field_id = models.ForeignKey(Fields, on_delete=models.CASCADE)


class PolicyList(models.Model):
    name = models.CharField(max_length=60)
    risk_type_id = models.ForeignKey(RiskTypeList, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.name


'''
Field_type
    id
    name Text, Number, 

Fields
	id
	risk_type_id
	field_name
	field_type_id
	enumerate
	enum_variants

risk_types_list
	id
	name

policy_list
	id
	name 3UPP risk_types_list.name + date
	risk_type_id
	date

'''
