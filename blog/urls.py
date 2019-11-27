from django.urls import path
from blog import views


app_name = "blog"

urlpatterns = [
    path('posts/', views.PostListView.as_view()),
    path('posts/<int:pk>/', views.PostDetailView.as_view()),
]