from django.urls import path
from .views import DisciplineListView, QuestionOrderListView, DisciplineDetailView,\
                   QuestionOrderDetailView, CreateDisciplineView, CreateQuestionOrderView,\
                   DisciplineUpdateView, QuestionOrderUpdateView, DeleteDisciplineView, DeleteOrderView

urlpatterns = [
    path('disciplines/', DisciplineListView.as_view(), name='disciplines'),
    path('orders/', QuestionOrderListView.as_view(), name='orders'),
    path('discipline/<int:pk>/', DisciplineDetailView.as_view(), name='discipline-detail'),
    path('order/<int:pk>/', QuestionOrderDetailView.as_view(), name='order-detail'),
    path('new-discipline/', CreateDisciplineView.as_view(), name='new-discipline'),
    path('new-order/', CreateQuestionOrderView.as_view(), name='new-order'),
    path('discipline/<int:pk>/update/', DisciplineUpdateView.as_view(), name='update-discipline'),
    path('order/<int:pk>/update/', QuestionOrderUpdateView.as_view(), name='update-order'),
    path('discipline/<int:pk>/delete/', DeleteDisciplineView.as_view(), name='delete-discipline'),
    path('order/<int:pk>/delete/', DeleteOrderView.as_view(), name='delete-order'),
]
