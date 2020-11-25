
from django.urls import path
from .views import service
# from . import views
urlpatterns = [
    path('service/<int:pk>',service,name='service'),
    
]
