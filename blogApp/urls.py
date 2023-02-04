from django.urls import path

from .views import BlogDetail, BlogList
urlpatterns = [
    path('blog_list', BlogList.as_view(), name='Blog Get'),
    path('blog_details/<int:pk>/', BlogDetail.as_view()),
]