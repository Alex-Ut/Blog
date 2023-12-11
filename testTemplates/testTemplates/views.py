
from django.shortcuts import render

MENU = {"Главная":"/", "Страница постов":"/catalog", "О блоге":"/about"}
def main_page(request):
    title = "Главная страница"
    data = {"menu" :MENU, "title": title}
    return render(request, './index.html', context=data)




def about_page(request):
    title = "О блоге"
    data = {"menu" :MENU, "title": title}
    return render(request, './about.html', context=data)