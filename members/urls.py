from django.urls import path
from .views import user
urlpatterns = [ 
   path('register/',user.as_view(), name='register')
]