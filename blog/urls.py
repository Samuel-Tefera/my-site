from django.urls import path

from . import views

urlpatterns = [
    path('', views.StartPageView.as_view(), name='home-page'),
    path('samuel-all-posts', views.AllPostPageView.as_view(), name='all-posts'),
]
