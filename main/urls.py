from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts', views.about, name='contacts'),
    path('new_contact', views.new, name='new_contacts'),
]
