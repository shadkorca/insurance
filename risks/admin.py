from django.contrib import admin
from .models import Fields, FieldTypes, RiskTypeList, PolicyList
# Register your models here.

admin.site.register(Fields)
admin.site.register(FieldTypes)
admin.site.register(RiskTypeList)
admin.site.register(PolicyList)
