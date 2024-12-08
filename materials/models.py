from django.db import models


class Course(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Введите название курса",
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание курса",
        help_text="Введите описание курса",
    )
    preview = models.ImageField(
        upload_to="materials/course_previews/",
        verbose_name="Превью",
        blank=True,
        null=True,
        help_text="Загрузите превью курса",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание урока",
        help_text="Введите описание урока",
    )
    preview = models.ImageField(
        upload_to="materials/lesson_previews/",
        verbose_name="Превью",
        blank=True,
        null=True,
        help_text="Загрузите превью урока",
    )
    link = models.URLField(
        null=True,
        blank=True,
        verbose_name="Ссылка на видео",
        help_text="Укажите ссылку на видео урока",
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="Курс", null=True, blank=True
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name
