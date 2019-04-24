from django.http import HttpResponse
from django.shortcuts import render
from crawlers.j_c import jumia_gaming, jumia_laptops, jumia_phones
from crawlers.k_c import konga_gaming, konga_laptops, konga_phones
from .utils import black_rock

# Create your views here.


def index(request):
    black_rock()
    return HttpResponse(f'It worked')


def j_gr(request):
    jumia_gaming()
    return HttpResponse('now')


def j_lr(request):
    jumia_laptops()
    return HttpResponse('now')


def j_pr(request):
    jumia_phones()
    return HttpResponse('now')


def k_gr(request):
    konga_gaming()
    return HttpResponse('now')


def k_pr(request):
    konga_phones()
    return HttpResponse('now')


def k_kl(request):
    konga_laptops()
    return HttpResponse('now')
