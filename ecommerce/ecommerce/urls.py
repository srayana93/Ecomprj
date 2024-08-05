from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from accounts import views as account_views

def home(request):
    return HttpResponse("Home Page")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('register/', account_views.register, name='register'),  # Register URL
    path('login/', account_views.custom_login, name='login'),  # Login URL
    path('', home, name='home'),  # Placeholder for the home view
]

