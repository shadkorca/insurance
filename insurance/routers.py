# coding=utf-8

from django.urls import path
from rest_framework import routers
from risks.viewsets import RiskViewSet, PolicyViewSets, RiskFieldsView

router = routers.DefaultRouter()

router.register(r'risks', RiskViewSet)
router.register(r'policies', PolicyViewSets)

urlpatterns = router.urls

urlpatterns += [
    path(r'risks/fields/<int:pk>/', RiskFieldsView.as_view({'get': 'list', 'post': 'create'})),
    path(r'risks/fields/<int:pk>/<int:sk>', RiskFieldsView.as_view({'delete': 'destroy', 'get': 'list'}))
]


