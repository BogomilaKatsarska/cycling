from django import http
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, resolve_url
from cycling.cyclist.models import Cyclist


def index(request):
    return render(request, 'index.html')


def cyclist_details(request, pk):
    current_cyclist = Cyclist.objects.get(pk=pk)
    context = {
        'title': 'The app for cyclists',
        'current_cyclist': current_cyclist,
    }
    return render(request, 'cyclist/cyclist_details.html', context)


def cyclists_all(request):
    all_cyclists = Cyclist.objects.all()
    context = {
        'all_cyclists': all_cyclists,
    }
    return render(request, 'cyclist/cyclists_all.html', context)


def redirect_to_cyclists_comparison_page(request):
    return redirect('cyclist all')


def redirect_to_cyclist_instagram_page(request):
    to = 'https://www.instagram.com/'
    return redirect(to)


def show_not_found(request):
    return HttpResponseNotFound('This page cannot be found')
