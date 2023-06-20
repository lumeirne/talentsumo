from django.urls import path
from notes_api import views
urlpatterns = [
    path('', views.NoteList.as_view()),
    path('<int:pk>/', views.NoteDetail.as_view()),
  ]