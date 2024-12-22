from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Course, Lesson, Subscription
from .validators import validate_source


class LessonSerializer(ModelSerializer):
    description = serializers.CharField(validators=[validate_source])
    link = serializers.CharField(validators=[validate_source])

    class Meta:
        model = Lesson
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    description = serializers.CharField(validators=[validate_source])

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    lesson_quantity = SerializerMethodField()
    lessons_list = LessonSerializer(source="lesson_set", many=True, read_only=True)
    subscription = SerializerMethodField(source="subscription_course", read_only=True)

    def get_subscription(self, instance):
        user = self.context["request"].user
        return Subscription.objects.filter(user=user).filter(course=instance).exists()

    def get_lesson_quantity(self, course):
        lessons = Lesson.objects.filter(course=course).count()
        return lessons

    # def get_lessons_list(self, course):
    #    lessons = Lesson.objects.filter(course=course)
    #   return [lesson.name for lesson in lessons]

    class Meta:
        model = Course
        fields = (
            "name",
            "description",
            "lesson_quantity",
            "lessons_list",
            "subscription",
        )
