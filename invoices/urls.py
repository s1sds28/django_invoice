# invoices/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from invoices import views

urlpatterns = [
    path('invoices/', views.InvoiceList.as_view(), name='invoice-list'),
    path('invoices/<int:pk>/', views.InvoiceDetail.as_view(), name='invoice-detail'),
    path('invoices/<int:pk>/highlight/',
         views.InvoiceHighlight.as_view(), name='invoice-highlight'), # new
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
