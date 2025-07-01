from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('publications/', views.publications, name='publications'),
    path('post/<int:pk>/', views.post_details, name='post_detail'),
]
