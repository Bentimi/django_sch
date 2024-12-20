"""
URL configuration for sch project.

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
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from userApp.views import SignUpView, countDown
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', TemplateView.as_view(template_name = 'home.html'), name='home'),
    path('course/', TemplateView.as_view(template_name = 'courses.html'), name='course'),
    path('about/', countDown, name='about'),
    path('contact/', TemplateView.as_view(template_name = 'contact.html'), name='contact'),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'^accounts/signup/$', SignUpView.as_view(), name='signup'),
    re_path(r'^userApp/', include("userApp.urls")),
    re_path(r'^admissionApp/', include("admissionApp.urls")),
    re_path(r'^recordApp/', include("recordApp.urls")),
    re_path(r'^paymentApp/', include("paymentApp.urls")),
    re_path(r'^adminApp/', include("adminApp.urls")),
    path('nav/', TemplateView.as_view(template_name = 'side_nav.html'), name='nav'),
    
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)