from django.urls import path

from .views import TelegramUsersListCreateAPIView, TelegramUsersRetrieveDestroyAPIView, TelegramUsersFilteredRetriveAPIView


urlpatterns = [
    path('api/tgusers/', TelegramUsersListCreateAPIView.as_view()),
    path('api/tgusers/<int:pk>/', TelegramUsersRetrieveDestroyAPIView.as_view()),
    path('api/tgusers/date/<str:dates>/', TelegramUsersFilteredRetriveAPIView.as_view()),
]