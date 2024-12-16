from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import (
    LessonCreateAPIView,
    LessonDestroyAPIView,
    LessonListAPIView,
    LessonRetrieveAPIView,
    LessonUpdateAPIView,
)

from .views import CourseViewSet

router = SimpleRouter()
router.register(r"courses", CourseViewSet, basename="courses")

app_name = MaterialsConfig.name

urlpatterns = [
    path("lessons/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_detail"),
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path(
        "lesson/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lesson_delete"
    ),
    path("lesson/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lesson_update"),
] + router.urls


# http://127.0.0.1:8000/courses/ through body/raw/json post
