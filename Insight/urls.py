"""
URL configuration for Insight project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from main import views
from django.contrib.auth import views as authentication_views
from users import views as user_views
from rest_framework.routers import DefaultRouter
from main.views import DocumentViewset
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


router = DefaultRouter()
router.register(r'documents', DocumentViewset, basename='document')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("register/", user_views.register, name="register"),
    path("login/", authentication_views.LoginView.as_view(template_name="users/login.html"),
        name="login"),  # for as view: the place wher you should search for the tamplate
    path("logout/", authentication_views.LogoutView.as_view(
        template_name="users/logout.html"), name="logout"),

    # Swagger UI.
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'),
]
