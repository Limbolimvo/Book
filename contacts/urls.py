from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'api/contacts', views.ContactViewSet)


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contacts', views.ContactsList.as_view(), name='contacts'),
    path('new-contact', views.AddContact.as_view(), name='new_contact'),
    path('contact/<int:pk>/', views.ContactDetail.as_view(), name='contact_details'),
    path('contact/edit/<int:pk>', views.ContactUpdate.as_view(), name='update_contact'),
    path('contact/delete/<int:pk>', views.ContactDelete.as_view(), name='delete_contact'),
    path('search_result', views.SearchResultsView.as_view(), name='search'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
