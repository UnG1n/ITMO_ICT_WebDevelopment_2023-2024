!!! example "Задание"
    После сериализаторов необходимо прописать представления (views.py) - основную логику сайта

=== "Импорты"

    ``` py
    from rest_framework import generics, viewsets
    from .models import Airplane, Flight, CrewMember, TransitStop, Employee
    from .serializers import AirplaneSerializer, FlightSerializer, CrewMemberSerializer, TransitStopSerializer, \
        EmployeeSerializer
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth import login as auth_login
    from django.views.generic.edit import FormView
    from django.urls import reverse_lazy
    from django.http import HttpResponseRedirect

    ```
    Для создания представлений нам требуется ссылаться практически на весь остальной наш код, поэтому именно в этом разделе 
    наибольшее количество импортов
    
=== "Регистрация"

    ``` py
    class UserCreateView(FormView):
        template_name = 'register.html'
        form_class = UserCreationForm
        success_url = reverse_lazy('token_create')
    
        def form_valid(self, form):
            user = form.save()
            auth_login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())

    ```
    Определяем класс UserCreateView, который наследуется от FormView Django и используется для создания нового пользователя в системе.
    name - поле типа CharField с максимальной длиной в 255 символов, предназначенное для хранения имени конференции.

    Атрибут template_name указывает на шаблон, который будет использоваться для отображения формы регистрации нового пользователя.

    Атрибут form_class определяет класс формы, которая будет использоваться для создания нового пользователя. 
    В данном случае, используется стандартный класс UserCreationForm Django, который включает поля для ввода имени пользователя, адреса электронной почты и пароля.

    Атрибут success_url указывает на URL-адрес, на который будет перенаправлен пользователь после успешного создания учетной записи. 
    В данном случае, после успешного создания учетной записи пользователь будет перенаправлен на страницу создания токена авторизации.

    Метод form_valid() вызывается, когда форма проходит проверку валидности. В этом методе создается новый пользователь с 
    помощью метода form.save(), а затем пользователь автоматически аутентифицируется с помощью функции auth_login(). 
    После этого пользователь перенаправляется на страницу создания токена авторизации с помощью метода get_success_url().


=== "Простые представления"

    ``` py
    class AirplaneViewSet(viewsets.ModelViewSet):
        queryset = Airplane.objects.all()
        serializer_class = AirplaneSerializer
    
    
    class AirplaneDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Airplane.objects.all()
        serializer_class = AirplaneSerializer
    
    
    class FlightViewSet(viewsets.ModelViewSet):
        queryset = Flight.objects.all()
        serializer_class = FlightSerializer
    
    
    class FlightDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Flight.objects.all()
        serializer_class = FlightSerializer
    
    
    class CrewMemberViewSet(viewsets.ModelViewSet):
        queryset = CrewMember.objects.all()
        serializer_class = CrewMemberSerializer
    
    
    class CrewMemberDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = CrewMember.objects.all()
        serializer_class = CrewMemberSerializer
    
    
    class TransitStopViewSet(viewsets.ModelViewSet):
        queryset = TransitStop.objects.all()
        serializer_class = TransitStopSerializer
    
    
    class TransitStopDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = TransitStop.objects.all()
        serializer_class = TransitStopSerializer
    
    
    class EmployeeViewSet(viewsets.ModelViewSet):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerializer
    
    
    class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerializer


    ```

    Остальные модели легче в представлении. Для каждой модели определены два класса представлений: ViewSet и DetailView.
    
    Класс ViewSet предоставляет стандартные CRUD-операции (создание, чтение, обновление и удаление) для модели. 
    Он наследуется от класса ModelViewSet Django REST framework и определяет атрибуты queryset и serializer_class.

    Атрибут queryset определяет набор объектов модели, которые будут доступны через представление.

    Атрибут serializer_class определяет класс сериализатора, который будет использоваться для преобразования объектов модели в 
    JSON и обратно.

    Класс DetailView предоставляет операции чтения, обновления и удаления для конкретного объекта модели. 
    Он наследуется от класса RetrieveUpdateDestroyAPIView Django REST framework и также определяет атрибуты queryset и 
    serializer_class.
