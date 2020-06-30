from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.theory_page, name='theory_page'),
    path('practice/', views.practice_page, name='practice_page'),
    path('info/', views.info_page, name='info_page')
]