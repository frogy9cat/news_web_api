from rest_framework import serializers
import pytz

from .models import News



class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'author', 'text', 'link', 'publishDateTime', 'created_at', 'updated_at')
        extra_kwargs = {
            'title': {'required': True},
            'text': {'required': True},
            'publishDateTime': {'required': False},

            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
        DateTimeValue = serializers.DateTimeField(default_timezone=pytz.utc)


    def create(self, validated_data):
        if 'publishDateTime' not in validated_data:
            validated_data['publishDateTime'] = None

        return News.objects.create(**validated_data)