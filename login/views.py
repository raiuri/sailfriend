import datetime
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

JWT_SECRET = settings.SECRET_KEY
JWT_ALGORITHM = 'HS256'

JWT_EXP_DELTA_SECONDS = 900 # 15 minutes
REFRESH_JWT_EXP_DELTA_DAYS = 7

# Temporary view, consider delete after configure all authentication flow.
class ProtectedView(APIView):
    def get(self, request):
        content = {"message": "You have permission to access this view!"}
        return Response(content, status=status.HTTP_200_OK)
