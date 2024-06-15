from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm
from theblog.models import Profile

# Widok edycji strony profilu
class EditProfilePageView(generic.UpdateView):
    model = Profile  # Model używany do edycji
    template_name = 'registration/edit_profile_page.html'  # Szablon używany do renderowania widoku
    fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url']  # Pola, które będą edytowane
    success_url = reverse_lazy('home')  # URL do przekierowania po pomyślnym zapisaniu formularza

# Widok rejestracji użytkownika
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm  # Formularz używany do rejestracji
    template_name = 'registration/register.html'  # Szablon używany do renderowania widoku
    success_url = reverse_lazy('login')  # URL do przekierowania po pomyślnej rejestracji

# Widok edycji profilu użytkownika
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm  # Formularz używany do edycji profilu
    template_name = 'registration/edit_profile.html'  # Szablon używany do renderowania widoku
    success_url = reverse_lazy('home')  # URL do przekierowania po pomyślnym zapisaniu formularza

    def get_object(self):
        # Zwraca aktualnie zalogowanego użytkownika jako obiekt do edycji
        return self.request.user
