"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("blog/", include("blog.urls")),
    path("", RedirectView.as_view(url="/blog/", permanent=True)),
    path("detail/", include("blog.urls")),
    path("recommend/", include("blog.urls")),
    path("about/", include("blog.urls")),
    path("cover/", include("blog.urls")),
    path("result/", include("blog.urls")),
    path("signup/", include("blog.urls")),
    path("login/", include("blog.urls")),
    path("coin/", include("blog.urls")),
    path("btc/", include("blog.urls")),
    path("ada/", include("blog.urls")),
    path("doge/", include("blog.urls")),
    path("omg/", include("blog.urls")),
    path("bch/", include("blog.urls")),
    path("eos/", include("blog.urls")),
    path("snt/", include("blog.urls")),
    path("eth/", include("blog.urls")),
    path("xrp/", include("blog.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
