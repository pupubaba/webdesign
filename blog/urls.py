from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('notices/', views.notice_home, name='notice_home'),
    path('notices/<int:pk>/', views.notice_detail, name='notice_detail'),
    path('notices/new/', views.notice_create, name='notice_new'),
    path('notices/delete/<int:pk>', views.notice_detail, name='notice_delete'),
    path('notices/update/<int:pk>', views.notice_update, name="notice_update"),
    path('free/', views.free_home, name='free_home'),
    path('free/<int:pk>/', views.free_detail, name='free_detail'),
    path('free/new/', views.free_create, name='free_new'),
    path('free/delete/<int:pk>', views.free_detail, name='free_delete'),
    path('free/update/<int:pk>', views.free_update, name="free_update"),
    path('tip/', views.tip_home, name='tip_home'),
    path('tip/<int:pk>/', views.tip_detail, name='tip_detail'),
    path('tip/new/', views.tip_create, name='tip_new'),
    path('tip/delete/<int:pk>', views.tip_detail, name='tip_delete'),
    path('tip/update/<int:pk>', views.tip_update, name="tip_update"),
]
