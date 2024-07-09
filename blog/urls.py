from django.urls import path

from . import views

urlpatterns = [
    path('', views.StartPageView.as_view(), name='home-page'),
    path('samuel-all-posts', views.AllPostPageView.as_view(), name='all-posts'),
    path('post/<slug:slug>', views.PostDetailPage.as_view(), name='post-detail'),
    path('stored-post', views.StoredPostView.as_view(), name='stored-post')
]
