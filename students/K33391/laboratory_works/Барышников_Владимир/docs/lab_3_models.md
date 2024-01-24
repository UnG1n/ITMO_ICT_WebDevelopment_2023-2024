!!! example "Задание"
    Необходимо описать базу данных средствами Django ORM

Для этого перейдём в файл models.py в нашем приложении и создадим несколько классов, наследуемых от django.db.models.Model. 

=== "Самолет"

    ``` py
    class Airplane(models.Model):
        number = models.CharField(max_length=50)
        type = models.CharField(max_length=50)
        seats = models.PositiveIntegerField()
        speed = models.FloatField()
        carrier_company = models.CharField(max_length=50)

    ```
    Описание класса -  Airplane - это класс представляющий модель самолета для нашего приложения
    
    У него есть несколько полей, таких как number (номер), type (тип), seats (количество мест), speed (скорость) и carrier_company 
    (авиакомпания-перевозчик). Каждое поле соответствует определенному атрибуту самолета, который можно хранить в базе данных.
    
=== "Рейс"

    ``` py
    class Flight(models.Model):
        flight_number = models.CharField(max_length=50)
        distance = models.FloatField()
        departure_airport = models.CharField(max_length=50)
        destination_airport = models.CharField(max_length=50)
        departure_datetime = models.DateTimeField()
        arrival_datetime = models.DateTimeField()
        transit_stops = models.ManyToManyField('TransitStop', blank=True)
        sold_tickets = models.PositiveIntegerField()

    ```
    Описание класс - Flight это класс представляющий модель полета в системе управления авиаперевозками
    
    У него есть несколько полей, таких как flight_number (номер рейса), distance (расстояние), departure_airport 
    (аэропорт отправления), destination_airport (аэропорт назначения), departure_datetime 
    (дата и время отправления), arrival_datetime (дата и время прибытия), transit_stops (транзитные остановки) и 
    sold_tickets (количество проданных билетов).

    Этот класс может быть использован для хранения информации о рейсах, а также для управления данными, связанными с 
    авиаперевозками, такими как расписание рейсов, количество проданных билетов и другие аспекты авиаперевозок.

=== "Экипаж"

    ``` py
    class CrewMember(models.Model):
        name = models.CharField(max_length=100)
        age = models.PositiveIntegerField()
        education = models.CharField(max_length=100)
        experience = models.PositiveIntegerField()
        passport_data = models.CharField(max_length=50)

    ```

    Этот класс представляет модель члена экипажа в системе управления авиакомпании.
    
    У него есть несколько полей, таких как name (имя), age (возраст), education (образование), experience (опыт работы) и passport_data (паспортные данные).

=== "Остановка"

    ``` py
    class TransitStop(models.Model):
        airport = models.CharField(max_length=50)
        datetime = models.DateTimeField()

    ```

    Этот класс представляет модель транзитной остановки в системе управления авиаперевозками. У него есть два поля: 
    airport (аэропорт) и datetime (дата и время).

    Может использоваться для отслеживания информации о транзитных остановках в рамках конкретного рейса или на пути между аэропортами. 

=== "Сотрудники"

    ``` py
    class Employee(models.Model):
        name = models.CharField(max_length=100)
        age = models.PositiveIntegerField()
        education = models.CharField(max_length=100)
        experience = models.PositiveIntegerField()
        passport_data = models.CharField(max_length=50)
        is_airport_employee = models.BooleanField(default=False)

    ```
    
    Этот класс представляет модель сотрудника в системе управления персоналом, который может быть использован, например, в 
    авиаперевозочной компании. У этого класса есть несколько полей:  name (имя), age (возраст), education (образование),
    experience (опыт работы),  passport_data (паспортные данные),  is_airport_employee (является ли сотрудник аэропортовским сотрудником),
    
    Может использоваться для хранения информации о сотрудниках, их биографических данных, образовании и опыте работы. 
    Поле is_airport_employee позволяет различать между сотрудниками аэропорта и другими работниками, что может быть полезно для управления персоналом в авиационной компании.

После создания всех моделей нужно обязательно сделать миграции:

- python manage.py makemigrations
- python manage.py migrate

А так же создать суперпользователя:

- python manage.py createsuperuser