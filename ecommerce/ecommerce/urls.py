from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from accounts import views as account_views
from .views import home



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('shop/', include('shop.urls')),
    path('register/', account_views.register, name='register'),  # Register URL
    path('login/', account_views.custom_login, name='login'),  # Login URL
    path('', home, name='home'),  # Home view with name 'home'
    ]

