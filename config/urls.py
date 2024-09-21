from django.contrib import admin
from django.urls import path, include
from login.views import ProtectedView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/protected/', ProtectedView.as_view(), name='protected'),   
]
