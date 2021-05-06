from django.urls import path
from .views import home, CreateQuestionView, CreateAnswerView

urlpatterns = [
    path('', home, name='home'),
    path('new-question/', CreateQuestionView.as_view(), name='new-question'),
    path('new-question/answer/', CreateAnswerView.as_view(), name='new-answer'),
]
