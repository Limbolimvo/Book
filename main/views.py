from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    contacts = Person.objects.order_by('name')
    return render(request, 'main/about.html', {'title': 'Список контактов', 'contacts': contacts})


def new(request):
    if request.method == 'POST':  # если данные передаются методом ПОСТ
        form = PersonForm(request.POST, request.FILES)  # мы их получаем
        if form.is_valid():  # и если данные введены корректно, то сохраняем их следующей строкой
            form.save()
            return redirect('contacts')

    form = PersonForm()
    context = {
        'form': form
    }
    return render(request, 'main/new.html', context)


def show_contact(request, person_id):
    contact = Person.objects.get(pk=person_id)
    return render(request, 'main/show_contact.html',
                  {"contact": contact}
                  )


def update(request, person_id):
    contact = Person.objects.get(pk=person_id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('contacts')

    return render(request, 'main/update.html',
                  {'contact': contact,
                   'form': form})


def delete_contact(request, person_id):
    contact = Person.objects.get(pk=person_id)
    contact.delete()
    return redirect('contacts')



