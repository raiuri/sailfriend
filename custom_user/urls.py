from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InterestCategoryViewSet


router = DefaultRouter()
router.register(r'interest-category', InterestCategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]