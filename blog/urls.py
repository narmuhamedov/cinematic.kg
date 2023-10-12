from django.urls import path
from . import views

urlpatterns = [
    path('post_link/', views.postView, name='posts'),
    path('date/', views.get_curent_data),
]