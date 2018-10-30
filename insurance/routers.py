# coding=utf-8

from rest_framework import routers


from risks.viewsets import RiskViewSet, PolicyViewSets # , RiskDetails

router = routers.DefaultRouter()

router.register(r'risks', RiskViewSet, basename='risk')

router.register(r'policies', PolicyViewSets)

# router.register(r'risks/(?P<risk_id>\d+)', RiskDetails)

# router.register(r'risk_details', RiskDetails)

# from notes.views import NoteViewSet
#
# router = routers.DefaultRouter()
# router.register(r'notes', NoteViewSet)

urlpatterns = router.urls


