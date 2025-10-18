from django.urls import path

from Blog.views import blog_single, blog_view

app_name ="Blog"

urlpatterns = [
    path('',blog_view,name="index"),
    path('single',blog_single,name="single"),

]
