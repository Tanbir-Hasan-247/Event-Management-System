from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.dispatch import receiver

@receiver(post_save, sender=User)
def assign_role(sender, instance, created, **kwargs):
    if created:
        user_group, created = Group.objects.get_or_create(name='Participant')
        instance.groups.add(user_group)
        instance.save()


@receiver(post_save, sender=User)
def send_activation_email(sender, instance, created, **kwargs):
    if created:
        token = default_token_generator.make_token(instance)
        activation_url = f"{settings.FRONTEND_URL}/users/activate/{instance.pk}/{token}/"
        
        subject = "Activate Your Account"
        message = f"Hi {instance.username},\n\nPlease click the link below to activate your account:\n{activation_url}\n\nThank you!"
        recipient_list = [instance.email]
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)