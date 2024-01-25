from django.urls import path
from todo import views

urlpatterns = [
    path("", views.TodosListAPIView.as_view()),
    path("create", views.TodoCreateAPIView.as_view()),
    path("<int:pk>/update", views.TodoUpdateAPIView.as_view()),
    path("<int:pk>/delete", views.TodoDestroyAPIView.as_view()),
    path("<int:pk>", views.TodoRetrieveAPIView.as_view()),
]