from django.contrib import admin
from .models import Fields, FieldTypes, RiskTypeList, EnumerateVariants, PolicyList, \
    FieldValue
# Register your models here.

admin.site.register(Fields)
admin.site.register(FieldTypes)
admin.site.register(RiskTypeList)
admin.site.register(EnumerateVariants)
admin.site.register(PolicyList)
admin.site.register(FieldValue)
