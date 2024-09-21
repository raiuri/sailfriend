from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Temporary view, consider delete after configure all authentication flow.
class ProtectedView(APIView):
    def get(self, request):
        content = {"message": "You have permission to access this view!"}
        return Response(content, status=status.HTTP_200_OK)
