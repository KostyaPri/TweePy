from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainViews),
    path('tw/<pk>/', views.twViews),
]
