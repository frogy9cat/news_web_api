from rest_framework import serializers
import pytz

from .models import TelegramUsers



class TelegramUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUsers
        fields = ('id', 'full_name', 'username', 'telegram_id', 'phone_number', 'created_at', 'updated_at')
        extra_kwargs = {
            'telegram_id': {'required': True},

            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
        DateTimeValue = serializers.DateTimeField(default_timezone=pytz.utc)