from django.urls import path
from .views import dashboard, home, CreateQuestionView, CreateAnswerView, \
                   QuestionDetailView, UpdateAnswerView, UpdateQuestionView, \
                   QuestionListView, QuestionSearchView, DeleteQuestionView, QuestionListDownloadView

urlpatterns = [
    path('', home, name='home'),
    path('dashboard', dashboard, name='dashboard'),
    path('order/<int:question_order>/question/<int:id_by_order>/create/',
         CreateQuestionView.as_view(), name='new-question'),
    path('order/<int:question_order>/question/<int:id_by_order>/answer/create/',
         CreateAnswerView.as_view(), name='new-answer'),
    path('order/<int:question_order>/question/<int:id_by_order>/',
         QuestionDetailView.as_view(), name='question-detail'),
    path('question/<int:pk>/change/', UpdateQuestionView.as_view(), name='question-update'),
    path('question/<int:pk>/answer/change/', UpdateAnswerView.as_view(), name='answer-update'),
    path('questions/', QuestionListView.as_view(), name='question-list'),
    path('questions/search/', QuestionSearchView.as_view(), name='question-search'),
    path('question/<int:pk>/delete/', DeleteQuestionView.as_view(), name='question-delete'),
    path('order/<int:question_order>/download/', QuestionListDownloadView.as_view(), name='download-questions'),
]
