from django.urls import path
from core.views import health_check

app_name = "core"

urlpatterns = [
    path("health-check/", health_check),
]
