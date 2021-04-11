from django.urls import path
from django.urls import path  
from .views import home,search


urlpatterns = [ 
    path('', home, name='home'),
    path('search', home, name='search'),

    
]