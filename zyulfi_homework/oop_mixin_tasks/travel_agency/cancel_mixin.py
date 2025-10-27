# CancelMixin
# Метод: cancel_trip(trip)
from oop_mixin_tasks.travel_agency.trip import Trip


class CancelMixin:
    def cancel_trip(self, trip=Trip):
        trip.cancel()
