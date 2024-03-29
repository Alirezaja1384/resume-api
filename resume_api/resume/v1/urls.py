from django.urls import path
from .routes import ProfileRetrieveAPIView, router

app_name = "resume"
urlpatterns = [
    path("profile/", ProfileRetrieveAPIView.as_view()),
] + router.urls
