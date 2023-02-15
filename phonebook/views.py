from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
from rest_framework import viewsets, permissions

from .serializers import ContactSerializer


def home(request):
    return render(request, 'main/home.html')


def all_contacts(request):
    if request.user.is_authenticated:
        me = request.user.id
        contacts = Contact.objects.filter(owner=me).order_by('name')
        return render(request, 'main/all_contacts.html',{
                        'contacts': contacts
                       })
    else:
        return redirect('contacts')


def create_contact(request):
    if request.method == 'POST':  # если данные передаются методом ПОСТ
        form = ContactForm(request.POST, request.FILES)  # мы их получаем
        if form.is_valid():  # и если данные введены корректно, то сохраняем их следующей строкой
            contact = form.save(commit=False)
            contact.owner = request.user.id  # logged in user
            contact.save()
            return redirect('contacts')

    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'main/create_contact.html', context)


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
    if request.user.id == contact.owner:
        contact.photo.delete(save=True)
        contact.delete()
        messages.success(request, ("Contact Deleted!!"))
        return redirect('contacts')
    else:
        messages.success(request, ("You Aren't Authrized To Delete Thes Contact!!"))
        return redirect('contacts')


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]
