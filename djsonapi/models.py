from django.db import models

class User(models.Model):
    id = models.CharField(max_length = 60)
    real_name = models.CharField(max_length = 60)
    tz = models.CharField()

class ActivityPeriod(models.Model):
    user_id = models.ForeignKey(User, related_name = 'activity_periods')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()