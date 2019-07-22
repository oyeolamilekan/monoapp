from django.shortcuts import render
from shop.models import Shop

# Create your views here.


def get_shop_view(request, slug):
    shop_info = Shop.objects.get(slug=slug)
    return render(request, "index.html", context={"shop": shop_info})

