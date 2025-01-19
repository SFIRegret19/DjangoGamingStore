from django.shortcuts import render
from django.views.generic import TemplateView
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
    game_list = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    button_text = 'Купить'
    platform_page_link_text = 'Главная'
    catalog_page_link_text = 'Магазин'
    cart_page_link_text = 'Корзина'
    context = {
        'title': title,
        'pagename': pagename,
        'game_list': game_list,
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