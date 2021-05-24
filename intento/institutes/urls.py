from django.urls import path
from .views import CreateDiscipline, CreateMacro, CreateMicro, UpdateInstitute, UpdateDiscipline, UpdateMacro, \
    UpdateMicro, DeleteDiscipline, DeleteMacro, DeleteMicro, InstituteDetail, DisciplineDetail, MacroDetail, \
    MicroDetail, DisciplineList, MacroList, MicroList

urlpatterns = [
    path('institute/<int:pk>/discipline/create/', CreateDiscipline.as_view(), name='new-discipline'),
    path('institute/<int:institute>/discipline/<int:discipline>/macro/create/', CreateMacro.as_view(),
         name='new-macro'),
    path('institute/<int:institute>/discipline/<int:discipline>/macro/<int:macro>/micro/create/',
         CreateMicro.as_view(), name='new-micro'),
    path('institute/<int:institute>/update/', UpdateInstitute.as_view(), name='update-institute'),
    path('institute/<int:institute>/discipline/<int:discipline>/update/', UpdateDiscipline.as_view(),
         name='update-discipline'),
    path('institute/<int:institute>/discipline/<int:discipline>/macro/<int:macro>/update/',
         UpdateMacro.as_view(), name='update-macro'),
    path('institute/<int:institute>/discipline/<int:discipline>/macro/<int:macro>/micro/<int:micro>/update/',
         UpdateMicro.as_view(), name='update-micro'),
    path('institute/<int:institute>/discipline/<int:discipline>/delete/', DeleteDiscipline.as_view(),
         name='delete-discipline'),
    path('institute/<int:institute>/discipline/<int:discipline>/delete/', DeleteDiscipline.as_view(),
         name='delete-discipline'),
    path('institute/<int:institute>/discipline/<int:discipline>/macro/<int:macro>/delete/',
         DeleteMacro.as_view(), name='delete-macro'),
    path('institute/<int:institute>/discipline/<int:discipline>/macro/<int:macro>/micro/<int:micro>/delete/',
         DeleteMicro.as_view(), name='delete-micro'),
    path('institute/<int:institute>/', InstituteDetail.as_view(), name='institute-detail'),
    path('institute/<int:institute>/discipline/<int:discipline>/', DisciplineDetail.as_view(),
         name='discipline-detail'),
    path('institute/<int:institute>/discipline/<int:discipline>/macro/<int:macro>/', MacroDetail.as_view(),
         name='macro-detail'),
    path('institute/<int:institute>/discipline/<int:discipline>/macro/<int:macro>/micro/<int:micro>/',
         MicroDetail.as_view(), name='micro-detail'),
    path('institute/<int:institute>/disciplines/', DisciplineList.as_view(), name='discipline-list'),
    path('institute/<int:institute>/discipline/<int:discipline>/macros/', MacroList.as_view(), name='macro-list'),
    path('institute/<int:institute>/discipline/<int:discipline>/macro/<int:macro>/micros/',
         MicroList.as_view(), name='micro-list'),
]
