from django.urls import path, include
from .views import movie_list, seat_list, booking_history, home
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'api/movies', MovieViewSet)
router.register(r'api/seats', SeatViewSet)
router.register(r'api/bookings', BookingViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('movies/', movie_list, name='movie_list'),
    path('seat_booking/', seat_list, name='seat_booking'),
    path('booking_history/', booking_history, name='booking_history'),
    path('api/', include(router.urls)),
]