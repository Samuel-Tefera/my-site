from django.urls import path

from . import views

urlpatterns = [
    path('', views.start_page, name='home-page'),
    path('samuel-all-posts', views.all_post_page, name='all-posts')
]
