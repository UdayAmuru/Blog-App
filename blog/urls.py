from django.urls import path
from .views import HomeView , ArticleDetailView, AddPostView, UpdatePostView , DeletePost , AddCategoryView , CategoryView, CategoryListView , LikeView , AddCommentView 
#from django.contrib.auth import views as auth_view
from members.views import *
urlpatterns = [
    #path('',views.home,name='home'),
    path('',HomeView.as_view(), name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/',AddPostView.as_view(),name='add_post'),
    path('add_category/',AddCategoryView.as_view(),name='add_category'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete',DeletePost.as_view(), name='delete_post'),
    path('category/<str:cats>/',CategoryView,name='category'),
    path('category-list/',CategoryListView,name='category-list'),
    path('like/<int:pk>',LikeView,name = 'like_post'),
    #path('<int:pk>/password/',auth_view.PasswordChangeView.as_view(template_name = 'registration/change-password.html')),
    path('<int:pk>/password/',PasswordsChangeView.as_view(template_name = 'registration/change-password.html')),
     path('<int:pk>/add_commentt/',AddCommentView.as_view(),name='add_comment'),
    
    
    
    
]
