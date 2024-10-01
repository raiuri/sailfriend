from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InterestCategoryViewSet, InterestViewSet


router = DefaultRouter()
router.register(r'interest-category', InterestCategoryViewSet)
router.register(r'interest', InterestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]