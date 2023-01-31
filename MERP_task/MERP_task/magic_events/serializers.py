from rest_framework import serializers
from .models import Events


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'event_title', 'start_date', 'end_date']

