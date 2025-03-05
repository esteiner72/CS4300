"""
URL configuration for movie_theater_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from bookings.views import MovieViewSet, SeatViewSet, BookingViewSet, home
from django.conf import settings
from django.conf.urls.static import static
from bookings import views

router = DefaultRouter()

router.register(r'api/movies', MovieViewSet)
router.register(r'api/seats', SeatViewSet)
router.register(r'api/bookings', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='homepage'),
    path('', include(router.urls)),
     path('', include('bookings.urls')),
]
