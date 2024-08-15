from django.urls import path

from .views import NewsListCreateAPIView, NewsRetrieveDestroyAPIView, NewsFilteredRetriveAPIView, LatestNewsListAPIView


urlpatterns = [
    path('api/news/', NewsListCreateAPIView.as_view()),
    path('api/news/<int:pk>/', NewsRetrieveDestroyAPIView.as_view()),
    path('api/news/date/<str:dates>/', NewsFilteredRetriveAPIView.as_view()),
    path('api/news/latest3/', LatestNewsListAPIView.as_view()),
]