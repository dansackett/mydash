from datetime import datetime

from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from reminders.models import Reminder


class Command(BaseCommand):
    """Grab all the unsent reminders and check if they should be sent out. If so
    then send them out and mark them as read.

    """
    args = 'N/A'
    help = 'Sends mail for reminders'

    def handle(self, *args, **options):
        reminders = Reminder.objects.filter(sent=False)
        for reminder in reminders:
            # Make now timezone-aware for comparison
            now = timezone.make_aware(datetime.now(),
                                      timezone.get_default_timezone())
            if reminder.date < now:
                subject = 'Reminder: {}'.format(reminder.title)
                from_email = 'noreply@sackettsolutions.com'
                to_email = reminder.user.email
                message = reminder.description
                send_mail(subject, message, from_email, [to_email],
                          fail_silently=True)
                reminder.sent = True
                reminder.save()