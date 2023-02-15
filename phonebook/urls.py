from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'api/contacts', views.ContactViewSet)


urlpatterns = [
    path('', views.home, name='home'),
    path('contacts', views.all_contacts, name='contacts'),
    path('new_contact', views.create_contact, name='new_contact'),
    path('show_contact/<contact_id>', views.show_contact, name='show_contact'),
    path('update_contact/<contact_id>', views.update_contact, name='update_contact'),
    path('delete_contact/<contact_id>', views.delete_contact, name='delete_contact'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
