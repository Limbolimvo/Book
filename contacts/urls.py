from django.urls import path, include
from rest_framework import routers
from . import views

from .views import ContactListView, ContactDetailView

# router = routers.DefaultRouter()
# router.register(r'api/contacts', views.ContactViewSet)


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contacts', views.ContactsList.as_view(), name='contacts'),
    path('contact/create', views.AddContact.as_view(), name='create_contact'),
    path('contact/info/<int:pk>', views.ContactDetail.as_view(), name='contact_details'),
    path('contact/edit/<int:pk>', views.ContactUpdate.as_view(), name='update_contact'),
    path('contact/delete/<int:pk>', views.ContactDelete.as_view(), name='delete_contact'),
    path('search/result', views.SearchResultsView.as_view(), name='search'),
    # path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/contacts/list', ContactListView.as_view()),
    path('api/contact/info/<int:pk>', ContactDetailView.as_view()),

]
