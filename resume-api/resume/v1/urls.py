from django.urls import path
from .routes import ProfileRetrieveAPIView

app_name = "resume_v1"
urlpatterns = [
    path("profile/", ProfileRetrieveAPIView.as_view()),
]
