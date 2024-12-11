from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = PhoneNumberField(
        verbose_name="Телефон",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    city = models.CharField(
        max_length=50,
        verbose_name="Страна",
        blank=True,
        null=True,
        help_text="Введите назввание вашей страны",
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        blank=True,
        null=True,
        help_text="Загрузите свое фото",
    )

    # token = models.CharField(
    # max_length=100, verbose_name="Token", blank=True, null=True
    # )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    CASH = "Cash"
    TRANSFER = "Transfer"

    STATUS_CHOICES = [
        (CASH, "Наличные"),
        (TRANSFER, "Перевод на счет"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Платеж")
    date = models.DateField(auto_now_add=True)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Курс", null=True, blank=True
    )
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="Урок", null=True, blank=True
    )
    payment_sum = models.PositiveIntegerField(verbose_name="Платеж")
    payment_method = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default=CASH,
        verbose_name="Способ оплаты",
    )

    class Meta:
        verbose_name = "Способ оплаты"
        verbose_name_plural = "Способы оплаты"

    def __str__(self):
        return self.date
