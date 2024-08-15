from django.db import models
from django.db.models.signals import post_save



class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    author = models.CharField(max_length=150, blank=True, verbose_name="Автор")
    text = models.TextField(verbose_name="Содержание")
    link = models.CharField(max_length=255, blank=True, verbose_name="Ссылка")
    publishDateTime = models.DateTimeField(blank=True, verbose_name="Дата выхода новости(UTC)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "A new"
        verbose_name_plural = "News"


