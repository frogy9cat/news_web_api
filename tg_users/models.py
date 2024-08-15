from django.db import models


class TelegramUsers(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, blank=True)
    telegram_id = models.IntegerField(unique=True)
    phone_number = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = "Telegram bot user"
        verbose_name_plural = "Telegram bot users"