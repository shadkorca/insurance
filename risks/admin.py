from django.contrib import admin
from .models import Fields, FieldTypes, RiskTypeList, PolicyList, FieldValue

admin.site.register(Fields)
admin.site.register(FieldTypes)
admin.site.register(RiskTypeList)
admin.site.register(PolicyList)
admin.site.register(FieldValue)
