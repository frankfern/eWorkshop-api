"""Celery tasks."""

# Django
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# Celery
from .celery import app


@app.task(name='request_reset_password_email', max_retries=3)
def request_reset_password_email(email, token):
    subject = 'Request Reset Password'
    from_email = 'eWorkshop <noreply@eworkshop.com>'
    content = render_to_string(
        'emails/password_reset.html',
        {'token': token, 'user': email}
    )
    msg = EmailMultiAlternatives(subject, content, from_email, [email])
    msg.attach_alternative(content, "text/html")
    msg.send()
