from django.urls import path
from .views import home, records, success

app_name = 'sales'

urlpatterns = [
   path('', home),
   path('sales/', records, name='records'),
   path('success/', success, name='success'),  
]
