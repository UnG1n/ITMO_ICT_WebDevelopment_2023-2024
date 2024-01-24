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