from django import http
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, resolve_url, get_object_or_404
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


def cyclists_open_for_new_opportunities(request):
    cyclists_opportunities = Cyclist.objects.filter(open_for_new_opportunities=True)\
        .order_by('last_name', 'first_name')
    context = {
        'cyclists_opportunities': cyclists_opportunities,
    }
    return render(request, 'cyclist/cyclists_opportunities.html', context)


def delete_cyclist(request, pk):
    cyclist = get_object_or_404(Cyclist, pk=pk)
    cyclist.delete()
    return redirect('index')


def redirect_to_cyclists_comparison_page(request):
    return redirect('cyclist all')


def redirect_to_cyclist_instagram_page(request):
    to = 'https://www.instagram.com/'
    return redirect(to)


def show_not_found(request):
    return HttpResponseNotFound('This page cannot be found')
