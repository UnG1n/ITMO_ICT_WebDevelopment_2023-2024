!!! example "Задание"
    Необходимо зарегистрировать маршруты для админ-панели нашего приложения

=== "Маршруты - urls.py"

    ``` py
    from django.urls import path
    from rest_framework import routers
    from djoser.views import TokenCreateView, TokenDestroyView
    from .views import (
        AirplaneDetailView, FlightDetailView,
        CrewMemberDetailView, TransitStopDetailView,
        EmployeeDetailView, UserCreateView, AirplaneViewSet, FlightViewSet, CrewMemberViewSet, TransitStopViewSet,
        EmployeeViewSet
    )
    
    
    router = routers.DefaultRouter()
    
    
    router.register(r'airplanes', AirplaneViewSet, basename='airplane')
    router.register(r'flights', FlightViewSet, basename='flight')
    router.register(r'crewmembers', CrewMemberViewSet, basename='crewmember')
    router.register(r'transitstops', TransitStopViewSet, basename='transitstop')
    router.register(r'employees', EmployeeViewSet, basename='employee')
    
    
    urlpatterns = [
        path('airplanes/<int:pk>/', AirplaneDetailView.as_view(), name='airplane-detail'),
        path('flights/<int:pk>/', FlightDetailView.as_view(), name='flight-detail'),
        path('crewmembers/<int:pk>/', CrewMemberDetailView.as_view(), name='crewmember-detail'),
        path('transitstops/<int:pk>/', TransitStopDetailView.as_view(), name='transitstop-detail'),
        path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
        path('token/create/', TokenCreateView.as_view(), name='token-create'),
        path('token/destroy/', TokenDestroyView.as_view(), name='token-destroy'),
        path('register/', UserCreateView.as_view(), name='user-register'),
    ]
    
    urlpatterns += router.urls

    ```
    urlpatterns - список URL-маршрутов, которые связывают определенные URL с соответствующими представлениями.
    
    Путь register/ связан с представлением views.register и именуется register.
    И так далее, каждый путь связан с определенным представлением.

    Сначала импортируем необходимые модули, включая path из Django, routers из Django REST framework и представления из приложения.

    Затем создаем экземпляр DefaultRouter, который будет использоваться для автоматической генерации маршрутов URL на основе определенных классов представлений.

    Для каждой модели определяем маршрут URL для ее DetailView, который использует класс представления соответствующего типа. 
    Например, для модели Airplane используется AirplaneDetailView.

    Также определяем маршруты URL для создания и удаления токенов авторизации и регистрации пользователей.

    Наконец, используется метод router.urls для добавления автоматически сгенерированных маршрутов URL для каждого класса представления.
    Эти URL-маршруты обеспечивают связь между определенными адресами URL и соответствующими представлениями в нашем приложении
