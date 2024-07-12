from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home_from_app'),
    path('<int:info_id>/', views.details, name='detailed_info')
]
