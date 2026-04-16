from .models import Event
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
from django.core.mail import send_mail
from django.conf import settings
from django.dispatch import receiver


@receiver(m2m_changed, sender=Event.participants.through)
def send_rsvp_email(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        users = User.objects.filter(pk__in=pk_set)
        for user in users:
            subject="Event RSVP Confirmation"
            if instance in instance.participants.all():
                message=f"Hi {user.first_name},\n\nYou are registered for {instance.name} on {instance.date}."
            else:
                message=f"Hi {user.first_name},\n\nYou have successfully RSVP'd for {instance.name} on {instance.date}."
            recipient_list=[user.email]
            
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
        