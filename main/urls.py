from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts', views.about, name='contacts'),
    path('new_contact', views.new, name='new_contact'),
    path('show_contact/<person_id>', views.show_contact, name='show_contact'),
    path('update_contact/<person_id>', views.update, name='update_contact'),
    path('delete_contact/<person_id>', views.delete_contact, name='delete_contact')
]
