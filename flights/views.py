from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from datetime import datetime

from .models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer, BookingDetailsSerializer, UpdateBookingSerializer, RegisterSerializer, AdminUpdateBookingSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsOwner, IsValidd

class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class BookingsList(ListAPIView):
	serializer_class = BookingSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return Booking.objects.filter(user=self.request.user, date__gte=datetime.today())


class BookingDetails(RetrieveAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingDetailsSerializer
	permission_classes = [IsOwner]
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'


class UpdateBooking(RetrieveUpdateAPIView):
	queryset = Booking.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'
	serializer_class = AdminUpdateBookingSerializer
	permission_classes = [IsOwner, IsValidd]
	def get_serializer_class(self):
		if self.request.user.is_staff:
			return AdminUpdateBookingSerializer
		else:
			return UpdateBookingSerializer

			
			
			
			


class CancelBooking(DestroyAPIView):
	queryset = Booking.objects.all()	
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'
	permission_classes = [IsOwner, IsValidd]

class BookFlight(CreateAPIView):
	serializer_class = AdminUpdateBookingSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user, flight_id=self.kwargs['flight_id'])


class Register(CreateAPIView):
	serializer_class = RegisterSerializer
