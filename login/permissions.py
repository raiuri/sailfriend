# from django.conf import settings
# from rest_framework import permissions
# from rest_framework.exceptions import AuthenticationFailed

# class JWTAuthentication(permissions.BasePermission):
#     def authenticate(self, request):
#         access_token = request.COOKIES.get('access_token')
#         if access_token is None:
#             return None
        
#         try:
#             # token = token.split(' ')[1] if token.startswith('Bearer ') else token
            
#             # se necessario adicionar lógica para recuperar o usuário
#             # Exemplo: user = User.objects.get(id=payload['user_id'])
#             # Exemplo: user = User.objects.get(id=payload['user_id'])

#             payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms=['HS256'])
#             return (None, payload)
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Expired token.')
#         except jwt.InvalidTokenError:
#             raise AuthenticationFailed('Invalid token.')
    
#     def authenticate_header(self, request):
#         return 'Bearer'

# def has_permission(self, request, view):
#     user = self.authenticate(request)
#     if user:
#         request.user = user
#         return True
#     return False