from django.urls import path

from .views import HeadTemplateView, SubdivisionListView, SubdivisionEmployeesAjaxListView


urlpatterns = [
    path('', HeadTemplateView.as_view(), name='head'),
    path('subdivision-list/', SubdivisionListView.as_view(),
         name='subdivision-list'),
    path('subdivision-list/<int:pk>/employees/',
         SubdivisionEmployeesAjaxListView.as_view(),
         name='subdivision-employee-list')
]
