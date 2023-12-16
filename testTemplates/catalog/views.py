from django.shortcuts import render
from .models import Product, ProductComment


MENU = {"Главная":"/", "Страница постов":"/catalog", "О блоге":"/about"}

def catalog_page(request):
    products = Product.objects.all()
    title = "Страница постов"
    data = {"menu" :MENU, "title": title, "products": products}
    return render(request, "./catalog.html", context=data)


def add_comment_page(request):
    products = Product.objects.values("id", "name")
    title = "Добавить комментрий"
    add_comment = ProductComment.objects.filter(checkbox=True).order_by('-id')
    data = {"menu": MENU, "title": title, "products": products, "add_comment": add_comment}

    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        comment_text = request.POST.get('comment')
        product_id = request.POST.get('product')
        checkbox_value = request.POST.get('checkbox')

        if user_name and email and comment_text and product_id and checkbox_value:
            product = Product.objects.get(pk=product_id)
            ProductComment.objects.create(user_name=user_name, comment=comment_text, product=product, email=email, checkbox=checkbox_value)

    all_comments = ProductComment.objects.order_by('-id')
    data["all_comments"] = all_comments
    return render(request, "./add_comment.html", context=data)


def thanks_page(request):
    user_name = request.POST['user_name']
    comment = request.POST['comment']
    email = request.POST['email']
    product = Product.objects.get(pk=request.POST['product'])
    ProductComment.objects.create(user_name=user_name, comment=comment, product=product, email=email)
    title = "Страница благодарностей"
    data = {"menu" :MENU, "title": title, "user_name":user_name}
    return render(request, "./thanks.html", context=data)
