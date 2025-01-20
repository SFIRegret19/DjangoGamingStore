from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from task1.forms import UserRegister
from task1.models import Buyer, Game
# Create your views here.
def platform_page_index(request):
    title = 'platform'
    pagename = 'Главная страница'
    platform_page_link_text = 'Главная'
    catalog_page_link_text = 'Магазин'
    cart_page_link_text = 'Корзина'
    context = {
        'title': title,
        'pagename': pagename,
        'platform_page_link_text': platform_page_link_text,
        'catalog_page_link_text': catalog_page_link_text,
        'cart_page_link_text': cart_page_link_text
    }
    return render(request, './fourth_task/platform.html', context)

def catalog_page_index(request):
    title = 'games'
    pagename = 'Игры'
    games_list = Game.objects.all()
    button_text = 'Купить'
    platform_page_link_text = 'Главная'
    catalog_page_link_text = 'Магазин'
    cart_page_link_text = 'Корзина'
    context = {
        'title': title,
        'pagename': pagename,
        'games_list': games_list,
        'button_text': button_text,
        'platform_page_link_text': platform_page_link_text,
        'catalog_page_link_text': catalog_page_link_text,
        'cart_page_link_text': cart_page_link_text
    }
    return render(request, './fourth_task/games.html', context)

def cart_page_index(request):
    title = 'cart'
    pagename = 'Корзина'
    cart_content_text = 'Извините, ваша корзина пуста'
    platform_page_link_text = 'Главная'
    catalog_page_link_text = 'Магазин'
    cart_page_link_text = 'Корзина'
    context = {
        'title': title,
        'pagename': pagename,
        'cart_content_text': cart_content_text,
        'platform_page_link_text': platform_page_link_text,
        'catalog_page_link_text': catalog_page_link_text,
        'cart_page_link_text': cart_page_link_text
    }
    return render(request, './fourth_task/cart.html', context)

def base(request):
    return render(request, './fourth_task/menu.html')

def sign_up_by_html(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        try:
            age = int(age)  # Преобразуем возраст в число
        except ValueError:
            info['error'] = 'Возраст должен быть числом.'
            return render(request, './fifth_task/registration_page.html', context={'info': info})

        if password == repeat_password:
            if age >= 18:
                if (username not in [user.name for user in users]):
                    Buyer.objects.create(name=username, age=age)
                    return HttpResponse(f'Приветствуем, {username}!')
                else:
                    info['error'] = f'Пользователь уже существует: user - {username}'
            else:
                info['error'] = f'Вы должны быть старше 18 лет: age - {age}'
        else:
            info['error'] = f'Пароли не совпадают: password - {password}, repeat_password - {repeat_password}'
    else:
        info['error'] = 'Форма заполнена некорректно. Проверьте данные.'
    
    return render(request, './fifth_task/registration_page.html', context={'info': info})



def sign_up_by_django(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            
            # --- Обработка после POST
            try:
                age = int(age)  # Преобразуем возраст в число
            except ValueError:
                info['error'] = 'Возраст должен быть числом.'
                return render(request, './fifth_task/registration_page.html', context={'info': info, 'form': form})

            if password == repeat_password:
                if age >= 18:
                    if (username not in [user.name for user in users]):
                        Buyer.objects.create(name=username, age=age)
                        return HttpResponse(f'Приветствуем, {username}!')
                    else:
                        info['error'] = f'Пользователь уже существует: user - {username}'
                else:
                    info['error'] = f'Вы должны быть старше 18 лет: age - {age}'
            else:
                info['error'] = f'Пароли не совпадают: password - {password}, repeat_password - {repeat_password}'
        else:
            info['error'] = 'Форма заполнена некорректно. Проверьте данные.'

    else:
        form = UserRegister()  # Пустая форма для GET-запроса
    
    return render(request, './fifth_task/registration_page.html', context={'info': info, 'form': form})