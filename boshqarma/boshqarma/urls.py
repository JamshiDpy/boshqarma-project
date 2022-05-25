"""boshqarma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


from api import urls, views
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response


@api_view(["GET"])
@permission_classes((AllowAny,))
def api_root(request, format=None):
    rest = {
        "boshqarma-api":"http://62.209.143.146:8800/boshqarma/",
        "rahbariyat-api":"http://62.209.143.146:8800/rahbariyat/",
        "speciality-api": "http://62.209.143.146:8800/speciality/",
        "news-api": "http://62.209.143.146:8800/news/",
        "murojaat-api": "http://62.209.143.146:8800/murojaat/",
        "events-api": "http://62.209.143.146:8800/events/",
        "regions-api": "http://62.209.143.146:8800/regions/",
        "hujjatlar-api": "http://62.209.143.146:8800/hujjatlar/",
        "fotos-api": "http://62.209.143.146:8800/fotos/",
        "presentations-api": "http://62.209.143.146:8800/presentations/",
        "projects-api":"http://62.209.143.146:8800/projects/",
        "comments-api":"http://62.209.143.146:8800/comments/",
    }
    # for url in urls.urlpatterns:
    #     rest[f"{url.name}"] = f"http:{request.path}/{url}"

    return Response(rest, status=200)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", api_root, name="api-root"),
    path("", include('api.urls')),
    path("password/reset/", views.PasswordResetView.as_view(), name="password-reset-api"),
    path("password/reset/confirm/", views.PasswordResetConfirmView.as_view(), name="password-reset-confirm-api"),
    path("auth/", include('dj_rest_auth.urls')),
    path("auth/registration/", include('dj_rest_auth.registration.urls')),
]

urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
