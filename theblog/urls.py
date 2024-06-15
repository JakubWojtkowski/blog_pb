from django.urls import path
from .views import HomeView, LoginView, RegisterView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, CategoryView, AddCommentView, MakePostPublicView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove',DeletePostView.as_view(), name='delete_post'),
    path('article/public/<int:pk>',MakePostPublicView.as_view(), name='public_post'),
    path('category/<str:cats>/',CategoryView, name='category'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),

]
