from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .token import account_activation_token


def send_email_verify(user, domain):

    subject = 'Verify Your Email Address'
    message = render_to_string('email_template.html', {
        'user': user,
        'token': account_activation_token.make_token(user),
        'domain': domain,
    })
    email_from = settings.EMAIL_HOST_USER
    email_to = [user.email]
    send_mail(subject, message, email_from, email_to)