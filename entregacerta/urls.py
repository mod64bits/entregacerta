from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from apps.users import urls as users_url
from apps.core.urls import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('usuarios/', include(users_url)),
    path('admin/', admin.site.urls),
]
