!!! example "Задание"
    Реализовать админ-панель нашего приложения в папке admin.py

Далее необходимо зарегистрировать все модели. 
Чтобы дополнительно их настроить, создадим новые классы, наследуемые от admin.ModelAdmin 
и повесим на них декоратор @admin.register(НазваниеМодели).

=== "Самолет"

    ``` py
    @admin.register(Airplane)
    class AirplaneAdmin(admin.ModelAdmin):
        list_display = ('number', 'type', 'seats', 'speed', 'carrier_company')
        search_fields = ('number', 'type', 'carrier_company')
    ```
    Определяется пользовательский класс администратора AirplaneAdmin для модели AirplaneAdmin, который наследуется 
    от admin.ModelAdmin. 
    
    Внутри класса AirplaneAdmin определены два атрибута:
    list_display: Он определяет, какие поля модели будут отображаться на странице списка объектов в административной панели. 
    В данном случае указаны поля number, type, seats, speed и carrier_company.
    search_fields: Этот атрибут определяет, по каким полям будет осуществляться поиск объектов. 
    В данном случае указаны поля number, type и carrier_company, что позволит администраторам системы быстрее находить объекты модели Airplane по этим полям.

    полный список атрибутов доступных администратору
    ![](http://ung1n.github.io/ITMO_ICT_WebDevelopment_2023-2024/img/lab3/admin_full_menu.png)  



    
=== "Сотрудник"

    ``` py
       @admin.register(Employee)
    class EmployeeAdmin(admin.ModelAdmin):
        list_display = ('name', 'age', 'education', 'experience', 'passport_data', 'is_airport_employee')
        search_fields = ('name', 'passport_data')
        list_filter = ('is_airport_employee',)
    ```
    Определяем класс EmployeeAdmin, который представляет настройки административной панели для модели Employee.
    Атрибут list_display ConferenceAdmin определяет поля, которые будут отображаться в списке моделей в интерфейсе администратора.

    Внутри класса EmployeeAdmin определены следующие атрибуты:
    list_display: Он определяет, какие поля модели будут отображаться на странице списка объектов в административной панели. 
    В данном случае указаны поля name, age, education, experience, passport_data и is_airport_employee.

    search_fields: Этот атрибут определяет, по каким полям будет осуществляться поиск объектов. 
    В данном случае указаны поля name и passport_data, что позволит администраторам системы быстрее находить объекты модели Employee по этим полям.

    list_filter: Этот атрибут определяет, по каким полям можно фильтровать объекты. В данном случае указано поле

    is_airport_employee, что позволит администраторам быстро фильтровать сотрудников, которые являются работниками аэропорта.

    ![](http://ung1n.github.io/ITMO_ICT_WebDevelopment_2023-2024/img/lab3/change_employee.png)  



=== "Член_экипажа"

    ``` py
    @admin.register(CrewMember)
    class CrewMemberAdmin(admin.ModelAdmin):
        list_display = ('name', 'age', 'education', 'experience', 'passport_data')
        search_fields = ('name', 'passport_data')
    ```
    Определяем класс CrewMemberAdmin, который представляет настройки административной панели для модели CrewMember.

    Внутри класса CrewMemberAdmin определены следующие атрибуты:
    list_display: Он определяет, какие поля модели будут отображаться на странице списка объектов в административной панели. 
    В данном случае указаны поля name, age, education, experience и passport_data.

    search_fields: Этот атрибут определяет, по каким полям будет осуществляться поиск объектов. 
    В данном случае указаны поля name и passport_data, что позволит администраторам системы быстрее находить объекты модели CrewMember по этим полям.

    ![](http://ung1n.github.io/ITMO_ICT_WebDevelopment_2023-2024/img/lab3/is_airport_employee.png)

=== "Транзит"

    ``` py
    @admin.register(TransitStop)
    class TransitStopAdmin(admin.ModelAdmin):
        list_display = ('airport', 'datetime')
        search_fields = ('airport',)
        date_hierarchy = 'datetime'
    ```
     Регистрируем модель TransitStop в административном интерфейсе и создает пользовательский интерфейс для нее.

    Атрибут list_display определяет поля, которые будут отображаться в списке объектов TransitStop в административном интерфейсе. 
    В данном случае он включает поля airport и datetime.

    Атрибут search_fields определяет поля, по которым можно осуществлять поиск в административном интерфейсе с помощью строки поиска. 
    В данном случае включено только поле airport.

    Атрибут date_hierarchy определяет поле, которое будет использоваться для навигации по датам в административном интерфейсе. 
    В данном случае используется поле datetime.

=== "Экипаж"

    ``` py
    @admin.register(Flight)
    class FlightAdmin(admin.ModelAdmin):
        list_display = (
            'flight_number', 'departure_airport', 'destination_airport', 'departure_datetime', 'arrival_datetime',
            'sold_tickets')
        search_fields = ('flight_number', 'departure_airport', 'destination_airport')
        date_hierarchy = 'departure_datetime'
        filter_horizontal = ('transit_stops',)
    ```
     Атрибут list_display определяет поля, которые будут отображаться в списке объектов Flight в административном интерфейсе. 
    В данном случае он включает поля flight_number, departure_airport, destination_airport, departure_datetime, arrival_datetime и sold_tickets.

    Атрибут search_fields определяет поля, по которым можно осуществлять поиск в административном интерфейсе с помощью строки поиска. 
    В данном случае включены поля flight_number, departure_airport и destination_airport.

    Атрибут date_hierarchy определяет поле, которое будет использоваться для навигации по датам в административном интерфейсе. 
    В данном случае используется поле departure_datetime.

    Атрибут filter_horizontal определяет поля, которые будут отображаться в виде горизонтального списка при редактировании 
    объекта Flight в административном интерфейсе. В данном случае используется поле transit_stops.