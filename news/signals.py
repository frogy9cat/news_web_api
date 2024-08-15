from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from aiogram import Bot
import asyncio

from .models import News
from tg_users.models import TelegramUsers



@receiver(post_save, sender=News)
def create_publication(sender, instance, created, **kwargs): 

    if created:
        bot = Bot(token=str(settings.BOT_TOKEN))
        new = News.objects.get(pk=instance.id)
        text = f"New publication... \ntitle: {new.title}\ncontent: {new.text}"

        tg_users = TelegramUsers.objects.all()
        
        for tg_user in tg_users:
            tg_user_id = tg_user.telegram_id
            asyncio.run(bot.send_message(chat_id=tg_user_id, text=text))
    else:
        pass