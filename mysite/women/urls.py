from django.urls import path
from . import views

urlpatterns = [
    path('', views.WomenHome.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('myPosts/', views.ShowUserPosts.as_view(), name='myPosts'),
    path('UpdatePost/<slug:post_slug>/', views.PostUpdateView.as_view(), name='updatePost'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('contant/', views.ContactFormView.as_view(), name='contact'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('logout/', views.userLogout, name='logout'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.WomenCategory.as_view(), name='category'),
]
