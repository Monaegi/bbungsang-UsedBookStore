from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from config import celery_app

MyUser = get_user_model()


@celery_app.task(bind=True)
def task_send_email(mail_subject, mail_content, user_pk):
    user = MyUser.objects.get(pk=user_pk)
    send_mail(
        mail_subject,
        mail_content,
        'bbungsang@gmail.com',
        [user.username]
    )