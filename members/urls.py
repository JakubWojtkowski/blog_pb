from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserRegisterView, UserEditView, EditProfilePageView

# Lista URL patterns: definiuje mapowanie URL-ów na odpowiednie widoki
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('<int:pk>/edit_profile_page', EditProfilePageView.as_view(), name='edit_profile_page'),
]