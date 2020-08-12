from django.core.management.base import BaseCommand, CommandError
from djsonapi.models import User, ActivityPeriod
from datetime import datetime

class Command(BaseCommand):
    '''
    populatejson: Custom management command to populate the database
    with dummy data.
    '''
    def handle(self, *args, **options):
        DATETIME_FORMAT = "%b %d %Y  %I:%M%p"

        User.objects.all().delete()
        ActivityPeriod.objects.all().delete()

        usernames = ['Aia Patricia', 'John Rogers', 'Pankaj Kumar', 'Martino Lavezzi']
        tzs = ['Asia/Kolkata', 'Africa/Bissau', 'America/Detroit', 'Australia/Eucla']
        ids = ['W011C801', 'W011C802', 'W011C803', 'W011C804']
        activity_periods = [
            ('W011C801', 'Mar 10 2020  4:35PM', 'Mar 10 2020  10:25PM'),
            ('W011C801', 'Apr 06 2020  1:00AM', 'Apr 25 2020  02:25PM'),
            ('W011C802', 'Jun 10 2020  5:30AM', 'Jun 16 2020  09:36PM'),
            ('W011C802', 'Sep 09 2020  12:50PM', 'Sep 18 2020  06:11PM'),
            ('W011C803', 'Oct 04 2020  5:00PM', 'Dec 16 2020  09:36PM'),
            ('W011C803', 'Nov 09 2020  12:50PM', 'Nov 18 2020  06:11PM'),
            ('W011C804', 'Sep 11 2020  2:45PM', 'Sep 12 2020  6:45PM')
        ]
        for i in range(len(usernames)):
            user = User.objects.get_or_create(real_name = usernames[i], tz = tzs[i], id = ids[i])

        for x in activity_periods:
            activity_period = ActivityPeriod.objects.get_or_create(
                user = User.objects.filter(id = x[0])[0],
                start_time = datetime.strptime(x[1], DATETIME_FORMAT),
                end_time = datetime.strptime(x[2], DATETIME_FORMAT)
            )

        self.stdout.write(self.style.SUCCESS('Data populated successfully'))