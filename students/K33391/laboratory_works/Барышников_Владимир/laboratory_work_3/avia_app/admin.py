from django.contrib import admin
from avia_app.models import Airplane, Employee, CrewMember, TransitStop, Flight



@admin.register(Airplane)
class AirplaneAdmin(admin.ModelAdmin):
    list_display = ('number', 'type', 'seats', 'speed', 'carrier_company')
    search_fields = ('number', 'type', 'carrier_company')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'education', 'experience', 'passport_data', 'is_airport_employee')
    search_fields = ('name', 'passport_data')
    list_filter = ('is_airport_employee',)


@admin.register(CrewMember)
class CrewMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'education', 'experience', 'passport_data')
    search_fields = ('name', 'passport_data')


@admin.register(TransitStop)
class TransitStopAdmin(admin.ModelAdmin):
    list_display = ('airport', 'datetime')
    search_fields = ('airport',)
    date_hierarchy = 'datetime'


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = (
        'flight_number', 'departure_airport', 'destination_airport', 'departure_datetime', 'arrival_datetime',
        'sold_tickets')
    search_fields = ('flight_number', 'departure_airport', 'destination_airport')
    date_hierarchy = 'departure_datetime'
    filter_horizontal = ('transit_stops',)