from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('<int:pk>/edit-story/', views.EditView.as_view(), name='editStory'),
    path('<int:pk>/delete-story/', views.DeleteView.as_view(), name='deleteStory'),
    path('author/<str:username>', views.AuthorView.as_view(), name='authorView'),

]

# <int:slug>