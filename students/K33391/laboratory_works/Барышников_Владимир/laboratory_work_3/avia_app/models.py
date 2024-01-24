from django.db import models


class Airplane(models.Model):
    number = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    seats = models.PositiveIntegerField()
    speed = models.FloatField()
    carrier_company = models.CharField(max_length=50)


class Flight(models.Model):
    flight_number = models.CharField(max_length=50)
    distance = models.FloatField()
    departure_airport = models.CharField(max_length=50)
    destination_airport = models.CharField(max_length=50)
    departure_datetime = models.DateTimeField()
    arrival_datetime = models.DateTimeField()
    transit_stops = models.ManyToManyField('TransitStop', blank=True)
    sold_tickets = models.PositiveIntegerField()


class CrewMember(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    education = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    passport_data = models.CharField(max_length=50)


class TransitStop(models.Model):
    airport = models.CharField(max_length=50)
    datetime = models.DateTimeField()


class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    education = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    passport_data = models.CharField(max_length=50)
    is_airport_employee = models.BooleanField(default=False)