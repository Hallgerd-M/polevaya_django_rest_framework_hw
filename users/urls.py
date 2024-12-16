from rest_framework.routers import SimpleRouter

from users.apps import UsersConfig

from .views import PaymentViewSet

router = SimpleRouter()
router.register(r"payments", PaymentViewSet, basename="payments")

app_name = UsersConfig.name


urlpatterns = [] + router.urls
