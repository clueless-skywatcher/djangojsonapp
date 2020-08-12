from rest_framework import serializers
from .models import User, ActivityPeriod

class ActivityPeriodSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format = '%b %d %Y %-I:%M%p')
    end_time = serializers.DateTimeField(format = '%b %d %Y %-I:%M%p')
    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')

class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many = True)
    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_periods')