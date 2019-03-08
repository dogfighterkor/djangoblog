from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail' ),
	path('update/<int:pk>/', views.post_update, name='post_update'),
	path('write/', views.post_write, name='post_write'),
	path('save/', views.post_save, name='post_save'),
	path('delete/<str:id>/<int:pk>/', views.post_del, name='post_del'),
]
