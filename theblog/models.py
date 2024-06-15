from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField


# Model tagów
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Nazwa tagu

    def __str__(self):
        return self.name  # Reprezentacja tekstowa obiektu


# Model kategorii
class Category(models.Model):
    name = models.CharField(max_length=255)  # Nazwa kategorii

    def __str__(self):
        return self.name  # Reprezentacja tekstowa obiektu

    def get_absolute_url(self):
        return reverse('home')  # Przekierowanie po utworzeniu obiektu


# Model profilu użytkownika
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)  # Powiązanie z modelem użytkownika
    bio = models.TextField()  # Biografia użytkownika
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")  # Zdjęcie profilowe
    website_url = models.CharField(max_length=255, null=True, blank=True)  # Strona internetowa
    facebook_url = models.CharField(max_length=255, null=True, blank=True)  # URL do profilu na Facebooku
    twitter_url = models.CharField(max_length=255, null=True, blank=True)  # URL do profilu na Twitterze
    instagram_url = models.CharField(max_length=255, null=True, blank=True)  # URL do profilu na Instagramie

    def __str__(self):
        return str(self.user)  # Reprezentacja tekstowa obiektu


# Model posta
class Post(models.Model):
    title = models.CharField(max_length=255)  # Tytuł posta
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")  # Obraz nagłówkowy
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Powiązanie z autorem (użytkownikiem)
    body = RichTextField(blank=True, null=True)  # Treść posta
    post_date = models.DateTimeField(auto_now_add=True)  # Data utworzenia posta
    category = models.CharField(max_length=255, default='other')  # Kategoria posta
    isPrivate = models.BooleanField(default=False)  # Flaga prywatności posta

    def __str__(self):
        return self.title + ' | ' + str(self.author)  # Reprezentacja tekstowa obiektu

    def get_absolute_url(self):
        return reverse('home')  # Przekierowanie po utworzeniu obiektu


# Model komentarza
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)  # Powiązanie z postem
    author = models.CharField(max_length=255)  # Autor komentarza
    body = models.TextField()  # Treść komentarza
    date_added = models.DateTimeField(auto_now_add=True)  # Data dodania komentarza

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"  # Reprezentacja tekstowa obiektu
