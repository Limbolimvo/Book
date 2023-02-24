from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView

from .models import Contact
from .forms import ContactForm
from django.contrib import messages
from rest_framework import viewsets, permissions

from .serializers import ContactSerializer


def home(request):
    return render(request, 'main/home.html')


def all_contacts(request):
    if request.user.is_authenticated:
        current_user = request.user
        contacts = Contact.objects.filter(owner=current_user).order_by('name')
        return render(request, 'main/all_contacts.html', {
            'contacts': contacts
        })
    else:
        return redirect('contacts')


class AddContact(CreateView):
    model = Contact
    template_name = 'main/create_contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()
        return redirect('contacts')

    # def create_contact(request):
    #     if request.method == 'POST':  # если данные передаются методом ПОСТ
    #         form = ContactForm(request.POST, request.FILES)  # мы их получаем
    #         current_user = request.user
    #         if form.is_valid():  # и если данные введены корректно, то сохраняем их следующей строкой
    #             contact = form.save(commit=False)
    #             contact.owner = current_user  # logged in user
    #             contact.save()
    #             return redirect('contacts')


def show_contact(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    return render(request, 'main/show_contact.html',
                  {"contact": contact}
                  )


def update_contact(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    form = ContactForm(request.POST or None, request.FILES or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('contacts')

    return render(request, 'main/update_contact.html',
                  {'contact': contact,
                   'form': form})


def delete_contact(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    current_user = request.user
    if current_user == contact.owner:
        contact.photo.delete(save=True)
        contact.delete()
        messages.success(request, ("Contact Deleted!!"))
        return redirect('contacts')
    else:
        messages.success(request, ("You Aren't Authrized To Delete Thes Contact!!"))
        return redirect('contacts')


def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        contact = Contact.objects.filter(name__contains=searched)

        return render(request,
                      'main/search_contact.html',
                      {'searched': searched,
                       'contact': contact})
    else:
        return render(request,
                      'main/search_contact.html',
                      {})


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]
