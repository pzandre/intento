from django.urls import path
from .views import dashboard, home, CreateQuestionView, CreateAnswerView, \
                   QuestionDetailView, UpdateAnswerView, UpdateQuestionView, \
                   QuestionListView, QuestionSearchView, DeleteQuestionView

urlpatterns = [
    path('', home, name='home'),
    path('dashboard', dashboard, name='dashboard'),
    path('new-question/', CreateQuestionView.as_view(), name='new-question'),
    path('question/<int:pk>/answer/', CreateAnswerView.as_view(), name='new-answer'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('question/<int:pk>/change/', UpdateQuestionView.as_view(), name='question-update'),
    path('question/<int:pk>/answer/change/', UpdateAnswerView.as_view(), name='answer-update'),
    path('questions/', QuestionListView.as_view(), name='question-list'),
    path('questions/search/', QuestionSearchView.as_view(), name='question-search'),
    path('question/<int:pk>/delete/', DeleteQuestionView.as_view(), name='question-delete'),
]
