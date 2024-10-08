"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Django admin interface
    path("admin/", admin.site.urls),
    
    # User registration endpoint
    path("api/user/register/", CreateUserView.as_view(), name="register"), 
    
    # JWT token generation endpoint
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    
    # JWT token refresh endpoint
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    
    # Django Rest Framework authentication views
    path("api-auth/", include("rest_framework.urls")),

    # Include all URL patterns from the api app
    # This allows us to organize our API endpoints in a separate file
    path("api/", include("api.urls")),
]
