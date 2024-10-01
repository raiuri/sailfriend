from rest_framework import viewsets, permissions
from .models import InterestCategory, Interest
from .serializers import InterestCategorySerializer
from .permissions import IsAdminUserOrReadOnly

class InterestCategoryViewSet(viewsets.ModelViewSet):
    queryset = InterestCategory.objects.all()
    serializer_class = InterestCategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUserOrReadOnly]

