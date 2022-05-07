from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name='home'),
    path('contacts', views.contacts, name="contacts"),
    path('feedback', views.feedback, name='feedback')
]
