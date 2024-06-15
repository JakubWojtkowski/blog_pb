from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

# Formularz rejestracji użytkownika
class SignUpForm(UserCreationForm):
    # Dodanie pól do formularza
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))  # Pole email
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))  # Pole imienia
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))  # Pole nazwiska

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')  # Pola, które będą wyświetlane w formularzu

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # Dodanie klasy CSS do pól formularza
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

# Formularz edycji profilu użytkownika
class EditProfileForm(UserChangeForm):
    # Dodanie pól do formularza
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))  # Pole email
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))  # Pole imienia
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))  # Pole nazwiska
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))  # Pole nazwy użytkownika
    last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))  # Pole ostatniego logowania
    is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))  # Pole superużytkownika
    is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))  # Pole pracownika
    is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))  # Pole aktywności
    date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))  # Pole daty dołączenia

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined')  # Pola, które będą wyświetlane w formularzu
