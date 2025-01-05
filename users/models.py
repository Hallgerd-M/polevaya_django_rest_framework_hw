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

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        help_text="Введите пользователя",
    )
    date = models.DateField(auto_now_add=True)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        null=True,
        blank=True,
        help_text="Введите курс",
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="Урок",
        null=True,
        blank=True,
        help_text="Введите урок",
    )
    payment_sum = models.PositiveIntegerField(
        verbose_name="Платеж",
        help_text="Введите сумму платежа",
    )
    payment_method = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default=CASH,
        verbose_name="Способ оплаты",
        help_text="Выберите способ оплаты",
    )
    session_id = models.CharField(
        max_length=255,
        verbose_name="ID сессии",
        blank=True,
        null=True,
        help_text="Введите ID сессии",
    )
    payment_link = models.URLField(
        max_length=400,
        verbose_name="Ссылка на оплату",
        blank=True,
        null=True,
        help_text="Введите ссылку на оплату",
    )

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплата"

    def __str__(self):
        return self.payment_sum
