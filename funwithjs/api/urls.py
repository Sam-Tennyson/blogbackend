from django.urls import path
from . import views

urlpatterns = [
    path('topic-list/', views.TopicListAPI.as_view()),
    path('topic-list/', views.TopicListAPI.as_view()),
    path('topic-list/<int:id>', views.TopicListAPI.as_view()),
    path('question-list/', views.QuestionListAPI.as_view()),
    path('question-list/<int:id>', views.QuestionListAPI.as_view()),

]