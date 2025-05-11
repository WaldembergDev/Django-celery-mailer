from celery import shared_task
from services.email_service import send_mail
from time import sleep

@shared_task
def task_mail(name, title, recipients):
    send_mail(name=name, title=title, recipients=recipients)
