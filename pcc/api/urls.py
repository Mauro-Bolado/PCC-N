from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('militants/', views.militants_page, name='militants'),
    path('debts/', views.debts_page, name='debts'),
]