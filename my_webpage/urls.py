from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('Comment',views.Comment, name = 'Comment'),
    path('show_comment',views.all_comment, name = 'all_comment')
]