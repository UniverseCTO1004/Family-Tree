from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, FamilyMemberViewSet, RelationshipViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'family-members', FamilyMemberViewSet)
router.register(r'relationships', RelationshipViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
