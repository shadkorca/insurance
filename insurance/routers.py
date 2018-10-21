# coding=utf-8

from rest_framework import routers


from risks.viewsets import RiskViewSet
router = routers.DefaultRouter()
router.register(r'risks', RiskViewSet)

# from notes.views import NoteViewSet
#
# router = routers.DefaultRouter()
# router.register(r'notes', NoteViewSet)

urlpatterns = router.urls


