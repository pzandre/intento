from django.urls import path
from .views import dashboard, home, CreateQuestionView, CreateAnswerView, QuestionDetailView

urlpatterns = [
    path('', home, name='home'),
    path('dashboard', dashboard, name='dashboard'),
    path('new-question/', CreateQuestionView.as_view(), name='new-question'),
    path('question/<int:pk>/answer/', CreateAnswerView.as_view(), name='new-answer'),
    path('question/<int:pk>/', QuestionDetailView.as_view() , name='question-detail'),
]
