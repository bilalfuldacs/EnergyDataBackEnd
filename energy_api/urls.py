from django.urls import path
from .views import EnergyDataView

urlpatterns = [
    path('energy-data/', EnergyDataView.as_view(), name='energy-data'),
]