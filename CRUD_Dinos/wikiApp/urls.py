from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CustomLoginView

# URL patterns
urlpatterns = [
    # Páginas principais
    path('', views.index, name='index'),
    path('teste/', views.teste, name='teste'),
    
    # Autenticação
    path('login/', CustomLoginView.as_view(), name='login'),  # Página de login personalizada
    path('logout/', auth_views.LogoutView.as_view(next_page='/wiki/login/'), name='logout'),  # Logout com redirecionamento
    path('registro/', views.registro, name='registro'),  # Página de registro
    
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),  # Página do dashboard (requer login)
]
