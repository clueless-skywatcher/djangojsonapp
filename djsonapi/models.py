from django.db import models

class User(models.Model):
    id = models.CharField(max_length = 10, primary_key = True)
    real_name = models.CharField(max_length = 50)
    tz = models.CharField(max_length = 20)

class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, related_name = 'activity_periods', on_delete = models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
