from django.urls import path
from .views import OrderList, OrderDetail, CreateOrder, UpdateOrder, DeleteOrder,\
    CreateQuestion, QuestionDetail, UpdateQuestion, QuestionList, QuestionSearch, DeleteQuestion, QuestionsPDFList, \
    QuestionListDownload, load_discipline_details, load_macro_details, load_micro_details, load_teacher_details

urlpatterns = [
    path('orders/', OrderList.as_view(), name='orders'),
    path('order/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('order/create/', CreateOrder.as_view(), name='create-order'),
    path('order/<int:order>/update/', UpdateOrder.as_view(), name='update-order'),
    path('order/<int:order>/delete/', DeleteOrder.as_view(), name='delete-order'),
    path('order/<int:order>/question/<int:id_by_order>/create/', CreateQuestion.as_view(), name='create-question'),
    path('order/<int:order>/question/<int:id_by_order>/', QuestionDetail.as_view(), name='question-detail'),
    path('order/<int:order>/question/<int:pk>/update/', UpdateQuestion.as_view(), name='update-question'),
    path('questions/', QuestionList.as_view(), name='questions'),
    path('questions/search/', QuestionSearch.as_view(), name='question-search'),
    path('order/<int:order>/question/<int:question>/delete/', DeleteQuestion.as_view(), name='delete-question'),
    path('order/<int:pk>/questions/', QuestionsPDFList.as_view(), name='order-questions'),
    path('order/<int:pk>/questions/pdf-download/', QuestionListDownload.as_view(), name='pdf-download'),
    path('ajax/load-discipline-details/', load_discipline_details, name='ajax-load-discipline'),
    path('ajax/load-macro-details/', load_macro_details, name='ajax-load-macro'),
    path('ajax/load-micro-details/', load_micro_details, name='ajax-load-micro'),
    path('ajax/load-teacher-details/', load_teacher_details, name='ajax-load-teacher'),
]
