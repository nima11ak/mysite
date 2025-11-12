from django.urls import path
from . import views
from Blog.views import blog_single, blog_view

app_name ="Blog"

urlpatterns = [
    path('',views.blog_view, name="index"),
    path('post-<int:pid>/', views.test, name='test'),
    path('post-<str:pid>/', views.blog_single, name='blog_single'),

]
 