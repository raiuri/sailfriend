import datetime
import jwt
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


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        payload = {
            'user_id': user.id,
            'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds=JWT_EXP_DELTA_SECONDS),
            'iat': datetime.datetime.now(datetime.UTC),
        }
        token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)

        refresh_payload = {
            'user_id': user.id,
            'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=REFRESH_JWT_EXP_DELTA_DAYS),
            'iat': datetime.datetime.now(datetime.UTC),
        }
        refresh_token = jwt.encode(refresh_payload, JWT_SECRET, JWT_ALGORITHM)

        return Response({
            'access_token': token,
            'refresh_token': refresh_token
            }, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def refresh_token_view(request):
    refresh_token = request.data.get('refresh_token')

    if refresh_token is None:
        return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        payload = jwt.decode(refresh_token, JWT_SECRET, JWT_ALGORITHM)

        jwt_payload = {
            'user_id': payload['user_id'],
            'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds=JWT_EXP_DELTA_SECONDS),
            'iat': datetime.datetime.now(datetime.UTC),
        }
        access_token = jwt.encode(jwt_payload, JWT_SECRET, JWT_ALGORITHM)

        return Response({'access_token': access_token}, status=status.HTTP_200_OK)
    
    except jwt.ExpiredSignatureError:
        return Response({'error': 'Refresh token has expired'}, status=status.HTTP_401_UNAUTHORIZED)
    except jwt.InvalidTokenError:
        return Response({'error': 'Invalid refresh token'}, status=status.HTTP_401_UNAUTHORIZED)