from django.shortcuts import render, redirect
from .models import Client
from .forms import LoginForm
from .models import Automobile
from .models import Client

# Create your views here.
def tables_home(request):
    return render(request,  'tables/tables_home.html')

def lk_view(request):
    return render(request, 'tables/lk.html')

def signin(request):
    return render(request, 'tables/signin.html')

def signup(request):
    return render(request, 'tables/signup.html')

def auto_home(request):
    return render(request,  'tables/auto_home.html')


def lk_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone']

            try:
                client = Client.objects.get(phone_number=phone_number)
                return redirect('signin', name=client.name, phone_number=client.phone_number)
            except Client.DoesNotExist:
                return render(request, 'lk.html', {'error': 'Клиент не найден', 'form': form})
    else:
        form = LoginForm()

    return render(request, 'tables/lk.html', {'form': form})

def signin_view(request, name, phone_number):
    try:
        client = Client.objects.get(phone_number=phone_number)
        club_card = client.club_card.first()  # Получаем первую клубную карту
        bonuses = club_card.bonuses if club_card else 0  # Проверка на существование клубной карты
    except Client.DoesNotExist:
        bonuses = 0  # Обработка случая, когда клиент не существует
    return render(request, 'tables/signin.html', {'name': name, 'phone_number': phone_number, 'bonuses': bonuses})


def car_list(request):
    filter_price = request.GET.get('price')
    filter_brand = request.GET.get('brand')

    automobiles = Automobile.objects.all()

    if filter_price and filter_price != 'all':
        if filter_price == 'low':
            automobiles = automobiles.filter(cost__lt=500)
        elif filter_price == 'medium':
            automobiles = automobiles.filter(cost__gte=500, cost__lt=700)
        elif filter_price == 'high':
            automobiles = automobiles.filter(cost__gte=700)

    if filter_brand and filter_brand != 'all':
        automobiles = automobiles.filter(brand__iexact=filter_brand)

    return render(request, 'tables/auto_home.html', {'automobiles': automobiles})


def signup_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        years = request.POST['years']

        # Создание нового клиента
        new_client = Client(name=name, phone_number=phone_number, years=years)
        new_client.save()

        # Перенаправление на другую страницу после успешной регистрации
        return redirect("lk")  # замените на вашу страницу

    return render(request, 'tables/signup.html')
