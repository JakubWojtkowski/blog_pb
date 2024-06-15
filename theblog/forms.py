from django import forms
from .models import Post, Category, Comment

# Pobieranie wszystkich kategorii i tworzenie listy wyborów
choices = Category.objects.all().values_list('name', 'name')
choice_list = []

for item in choices:
    choice_list.append(item)

# Formularz tworzenia posta
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body', 'header_image', 'isPrivate')

        # Definiowanie widgetów dla pól formularza
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),  # Pole tytułu
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),  # Ukryte pole autora
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),  # Pole wyboru kategorii
            'body': forms.Textarea(attrs={'class': 'form-control'}),  # Pole treści posta
        }

# Formularz edycji posta
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'isPrivate')

        # Definiowanie widgetów dla pól formularza
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),  # Pole tytułu
            'body': forms.Textarea(attrs={'class': 'form-control'}),  # Pole treści posta
        }

# Formularz do publikowania posta
class EditPublicForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        # Definiowanie widgetów dla pól formularza
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),  # Ukryte pole tytułu
        }

# Formularz dodawania komentarza
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'body')

        # Definiowanie widgetów dla pól formularza
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),  # Ukryte pole autora
            'body': forms.Textarea(attrs={'class': 'form-control'}),  # Pole treści komentarza
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['author'].required = False  # Ustawienie pola autora jako opcjonalne
