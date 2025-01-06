from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from materials.models import Course, Subscription
from users.models import User


@shared_task
def send_update_email(course_id):
    """Sends email when course is updated"""
    course = Course.objects.filter(id=course_id).first()
    message = f"Курс '{course.name}' был обновлен. Смотрите изменения на сайте: http://127.0.0.1:8000/courses/{course.id}"
    email = course.owner.email
    send_mail("Обновление курса", message, EMAIL_HOST_USER, [email])


def send_updated_email_using_subscription(course_id):
    subscription = Subscription.objects.filter(course=course_id).first()
    message = f"Курс '{subscription.course.name}' был обновлен. Смотрите изменения на сайте: http://127.0.0.1:8000/courses/{subscription.course.id}"
    email = subscription.user.email
    send_mail("Обновление курса", message, EMAIL_HOST_USER, [email])


@shared_task
def make_user_inactive():
    """Changes flag is_active to False if user's last_login was more than a month ago"""
    today = timezone.now()
    users = User.objects.filter(is_superuser=False, last_login__isnull=False)
    for user in users:
        if today - user.last_login > timedelta(days=30):
            user.is_active = False
            user.save()
            print(f"Пользователь {user.email} заблокирован")
