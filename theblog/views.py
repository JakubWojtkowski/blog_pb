from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from django.urls import reverse_lazy, Resolver404
from .forms import PostForm, EditForm, CommentForm, EditPublicForm
import logging
from django.contrib.auth.mixins import LoginRequiredMixin
import django
from django.shortcuts import redirect
from django.urls import reverse

# Konfiguracja Django
django.setup()

# Konfiguracja loggera
logger = logging.getLogger(__name__)

# Widok strony głównej
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    cats = Category.objects.all()
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        # Pobiera dodatkowe dane kontekstowe do szablonu
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

# Widok dla kategorii
def CategoryView(request, cats):
    # Filtruje posty według kategorii
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})

# Widok szczegółów artykułu
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        # Pobiera dodatkowe dane kontekstowe do szablonu
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

# Widok dodawania posta
class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def form_valid(self, form):
        # Ustawia autora na zalogowanego użytkownika i zapisuje post
        form.instance.author = self.request.user
        self.object = form.save()
        post_id = self.object.pk
        logger.info(f'User id: {self.request.user.id} added a new post with title: {form.instance.title} and post ID: {post_id}')
        return redirect(self.get_success_url())

# Widok logowania
class LoginView(ListView):
    model = Post
    template_name = 'login.html'
    fields = '__all__'

# Widok rejestracji
class RegisterView(ListView):
    model = Post
    template_name = 'register.html'
    fields = '__all__'

# Widok edytowania posta
class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'update_post.html'

    def get_form_class(self):
        post = self.get_object()
        if post.isPrivate:
            return EditForm
        else:
            return EditPublicForm

    def form_valid(self, form):
        # Loguje edycję posta przez użytkownika
        logger.info(f'User {self.request.user.id} updated post ID: {self.kwargs.get("pk")}')
        return super().form_valid(form)

# Widok publikowania posta
class MakePostPublicView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'public_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Ustawia post na publiczny i zapisuje zmiany
        self.object = form.save(commit=False)
        self.object.isPrivate = False
        self.object.save()
        logger.info(f'User {self.request.user.id} made post ID: {self.object.pk} public')
        return super().form_valid(form)

# Widok usuwania posta
class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        # Loguje potwierdzenie usunięcia posta przez użytkownika
        logger.info(f'User {self.request.user.id} confirmed deletion of post ID: {self.kwargs.get("pk")}')
        return super().post(request, *args, **kwargs)

# Widok dodawania komentarza
class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        # Ustawia ID posta i autora komentarza na zalogowanego użytkownika
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user.username
        logger.info(f'User {self.request.user.id} added a new comment to post ID: {self.kwargs.get("pk")}')
        return super().form_valid(form)

    def get_success_url(self):
        try:
            # Przekierowuje na stronę szczegółów artykułu po dodaniu komentarza
            return reverse('article-detail', kwargs={'pk': self.kwargs['pk']})
        except Resolver404:
            # Przekierowanie na stronę główną jeśli URL jest nieprawidłowy
            return reverse_lazy('home')
