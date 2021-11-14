from django.urls import path

from blog import views
from blog.views import render_post, post_detail

app_name = 'blog'

urlpatterns = [

    path('', render_post, name='post'),
    path('<int:post_id>', post_detail, name='post_detail')

]
