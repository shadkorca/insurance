# coding=utf-8

from django.urls import path
from rest_framework import routers
from risks.viewsets import RiskViewSet, PolicyViewSets, RiskFieldsView, \
                            PolicyFieldsView

router = routers.DefaultRouter()

router.register(r'risks', RiskViewSet)
router.register(r'policies', PolicyViewSets)

urlpatterns = router.urls

urlpatterns += [
    path(r'risks/fields/<int:pk>/', RiskFieldsView.as_view({'get': 'list', 'post': 'create'})),
    path(r'risks/fields/<int:pk>/<int:sk>', RiskFieldsView.as_view({'delete': 'destroy', 'get': 'list'})),
    path(r'policies/fields/<int:pk>/', PolicyFieldsView.as_view({'get': 'list', 'post': 'create'})),
    path(r'policies/fields/<int:pk>/<int:sk>', PolicyFieldsView.as_view({'delete': 'destroy', 'get': 'list',
                                                                         'patch': 'partial_update'}))
]


