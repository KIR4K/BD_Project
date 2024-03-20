from django.shortcuts import render
from .models import Client,Passport
from django.shortcuts import redirect


app_name = 'client'

def form_1(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        patronymic = request.POST.get('patronymic')


        client = Client.objects.create(
            client_first_name=first_name,
            client_second_name=last_name,
            client_patronymic=patronymic

        )

        # Дальнейшие действия (например, сохранение клиента, редирект и т.д.)
        return redirect('form_2', client_id=client.id)
    return render(request, 'client/form_1.html')  # Замените 'your_template.html' на ваш шаблон

def form_2(request, client_id):
    client = Client.objects.get(pk=client_id)

    if request.method == 'POST':
        series = request.POST.get('passport_series')
        number = request.POST.get('passport_number')
        birth_date = request.POST.get('birth_date')
        address_1 = request.POST.get('address')

        passport = Passport.objects.create(
            client = client,
            passport_birth_date=birth_date,
            passport_series=series,
            passport_number=number,
            address = address_1,

        )
        # Дальнейшие действия (например, сохранение клиента, редирект и т.д.)
        return redirect('admin:index')  # Пример редиректа на страницу успеха
    return render(request, 'client/form_2.html',{'client': client})  # Замените 'your_template.html' на ваш шаблон
