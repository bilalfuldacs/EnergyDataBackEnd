from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Optional: Add a simple response for root URL
def home(request):
    return HttpResponse("Welcome to Energy API. Use /api/energy-data/ to access the data.")

urlpatterns = [
    path('', home, name='home'),  # Add this for root URL
    path('admin/', admin.site.urls),
    path('api/', include('energy_api.urls')),
]