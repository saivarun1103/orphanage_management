from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('manage_orphans/', views.manage_orphans, name='manage_orphans'),
]
