
from django.urls import path
from .views import Company,Contact
# from . import views
urlpatterns = [
    # path('',home,name='home'),
    # path('',Company.as_view(),name='company'),
    path('',Company,name='company'),
    path('contact/',Contact,name='contact')
]
