!!! example "Задание"
    Перед тем как писать представления, нам нужно создать для них сериализаторы. 

Для этого создадим файл serializers.py в наших приложениях.

=== "Create"

    ``` py
    class CustomTokenCreateSerializer(TokenCreateSerializer):

    def create(self, validated_data):
        token = super().create(validated_data)

        user = self.user
        token['user_id'] = user.id
        token['email'] = user.email

        return token

    ```
    Определяем класс с CustomTokenCreateSerializer, который наследуется от стандартного сериализатора Django REST Framework TokenCreateSerializer. 
    Он переопределяет метод create, который вызывается при создании токена аутентификации.
    
    Метод create получает валидированные данные из запроса и вызывает метод create родительского класса, чтобы создать токен. 
    Затем он получает объект пользователя из контекста запроса, добавляет его идентификатор и адрес электронной почты к токену и возвращает его.

    
=== "User"

    ``` py
    class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'is_active', 'date_joined')

    ```

    Определяем класс CustomUserSerializer, который наследуется от стандартного сериализатора Django REST Framework UserSerializer. 
    Он переопределяет класс Meta, чтобы задать список полей, которые будут сериализованы для объектов пользователя.

    В данном случае, CustomUserSerializer добавляет к стандартному списку полей (id, email, username, first_name,  
    last_name, is_active, date_joined) поле id. Это позволяет получать идентификатор пользователя при сериализации объектов, 
    что может быть полезно для различных целей, например, для связи с другими объектами в приложении.

=== "Простые сериализаторы"

    ``` py
    class AirplaneSerializer(serializers.ModelSerializer):
        class Meta:
            model = Airplane
            fields = '__all__'
    
    
    class FlightSerializer(serializers.ModelSerializer):
        class Meta:
            model = Flight
            fields = '__all__'
    
    
    class CrewMemberSerializer(serializers.ModelSerializer):
        class Meta:
            model = CrewMember
            fields = '__all__'
    
    
    class TransitStopSerializer(serializers.ModelSerializer):
        class Meta:
            model = TransitStop
            fields = '__all__'
    
    
    class EmployeeSerializer(serializers.ModelSerializer):
        class Meta:
            model = Employee
            fields = '__all__'

    ```
    Класс AirplaneSerializer наследуется от стандартного сериализатора ModelSerializer Django REST Framework и 
    определяет модель Airplane как модель для сериализации. Поле Meta определяет модель, которая будет сериализована, 
    и список полей, которые будут включены в сериализованный объект.  
    В данном случае, все поля модели Airplane будут включены в сериализованный объект.
    
    Аналогично, классы FlightSerializer, CrewMemberSerializer, TransitStopSerializer и EmployeeSerializer определяют модели Flight,    
    CrewMember, TransitStop и Employee соответственно как модели для сериализации и включают все поля каждой модели в 
    сериализованный объект.

    Таким образом, эти классы позволяют сериализовать объекты различных моделей в Django REST Framework, что может быть 
    полезно для передачи данных между клиентом и сервером в приложении.