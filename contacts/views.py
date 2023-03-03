from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Contact
from .forms import ContactForm
from rest_framework import viewsets, permissions, generics

from .permissions import IsOwner
from .serializers import ContactViewSerializer, ContactDetailSerializer

User = get_user_model()


class HomeView(ListView):
    model = User
    template_name = 'main/home.html'


class ContactsList(ListView):
    model = Contact
    template_name = 'main/all_contacts.html'

    def get_queryset(self, *args, **kwargs):
        qs = super(ContactsList, self).get_queryset(*args, **kwargs)
        current_user = self.request.user
        qs = qs.filter(owner=current_user).order_by("first_name")
        return qs


class AddContact(CreateView):
    model = Contact
    template_name = 'main/create_contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()
        return redirect('contacts')


class ContactDetail(DetailView):
    model = Contact
    template_name = 'main/show_contact.html'


class ContactUpdate(UpdateView):
    form_class = ContactForm
    model = Contact
    template_name = 'main/update_contact.html'


class ContactDelete(DeleteView):
    model = Contact
    success_url = reverse_lazy('contacts')
    template_name = "main/contact_confirm_delete.html"


class SearchResultsView(ListView):
    model = Contact
    template_name = 'main/all_contacts.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        current_user = self.request.user
        qs = Contact.objects.filter(owner=current_user)
        object_list = qs.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(phone__icontains=query)
        )
        return object_list


class ContactListView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactViewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactDetailSerializer
    permission_classes = [IsAuthenticated | IsOwner | IsAdminUser]

