from django.dispatch import receiver, Signal
from django.core.mail import send_mail
from django.urls import reverse
from config.settings.base import FRONT_URL

__all__ = [
    'reset_password_token_created',
    'post_password_reset',
]

reset_password_token_created = Signal(
    providing_args=["instance", "reset_password_token"],
)

post_password_reset = Signal(providing_args=["user"])


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "{}/?token={}".format(
        FRONT_URL, reset_password_token)

    send_mail(
        # title:
        subject="Password Reset for {title}".format(
            title="Reset Password for eworshop "),
        # message:
        message=email_plaintext_message,
        # from:
        from_email=None,
        # to:
        recipient_list=[instance.user.email]
    )
