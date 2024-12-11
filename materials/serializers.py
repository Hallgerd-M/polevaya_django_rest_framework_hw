from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(ModelSerializer):
    lesson_quantity = SerializerMethodField()
    # lessons_list = SerializerMethodField()
    lessons_list = LessonSerializer(source="lesson_set", many=True, read_only=True)

    def get_lesson_quantity(self, course):
        lessons = Lesson.objects.filter(course=course).count()
        return lessons

    # def get_lessons_list(self, course):
    #    lessons = Lesson.objects.filter(course=course)
    #   return [lesson.name for lesson in lessons]

    class Meta:
        model = Course
        fields = ("name", "description", "lesson_quantity", "lessons_list")
