from django.urls import path
from django.urls import path  
from .views import home,search, houses,schools,facilities,hospitals,markets,neighbours,recreation,events



urlpatterns = [ 
    path('', home, name='home'),
    path('search', search, name='search'),
    path('houses/', houses, name='houses'),
    path('schools/', schools, name='schools'),
    path('facilities/', facilities, name='facilities'),
    path('hospitals/', hospitals, name='hospitals'),
    path('markets/', markets, name='markets'),
    path('neighbours/', neighbours, name='neighbours'),
    path('recreation/', recreation, name='recreation'),
    path('events/', events, name='events'),

    
]