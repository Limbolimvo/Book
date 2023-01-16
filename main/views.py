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
        form = PersonForm(request.POST)  # мы их получаем
        if form.is_valid():  # и если данные введены корректно, то сохраняем их следующей строкой
            form.save()
            return redirect('contacts')

    form = PersonForm()
    context = {
        'form': form
    }
    return render(request, 'main/new.html', context)
