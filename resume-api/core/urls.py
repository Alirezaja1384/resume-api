"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

app_name = "core"


v1_routes = include(
    (
        [
            path(
                "admin/",
                include(
                    [
                        path("resume/", include("resume.admin.v1.urls")),
                    ]
                ),
            ),
            path("resume/", include("resume.v1.urls")),
            path("auth/", include("authentication.v1.urls")),
        ],
        "v1",
    ),
    namespace="v1",
)


schema_routes = include(
    [
        path("", SpectacularAPIView.as_view(), name="schema"),
        path(
            "docs/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="docs",
        ),
        path(
            "redoc/",
            SpectacularRedocView.as_view(url_name="schema"),
            name="redoc",
        ),
    ]
)

urlpatterns = [
    path("v1/", v1_routes),
    path("schema/", schema_routes),
]
