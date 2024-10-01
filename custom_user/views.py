from rest_framework import viewsets, permissions
from .models import InterestCategory, Interest
from .serializers import InterestCategorySerializer, InterestSerializer
from .permissions import IsAdminUserOrReadOnly

class InterestCategoryViewSet(viewsets.ModelViewSet):
    queryset = InterestCategory.objects.all()
    serializer_class = InterestCategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUserOrReadOnly]


class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUserOrReadOnly]
