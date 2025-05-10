from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def send_mail(name: str, title: str, recipients: list):
    html_contet = render_to_string(
        'emails/my_email.html',
        context={'name': name}
    )

    text_content = strip_tags(html_contet)

    msg = EmailMultiAlternatives(
        title,
        text_content,
        settings.DEFAULT_FROM_EMAIL,
        recipients,
        headers={'List-Unsubscribe': '<mailto:unsub@example.com>'}
    )

    msg.attach_alternative(html_contet, 'text/html')

    msg.send()

