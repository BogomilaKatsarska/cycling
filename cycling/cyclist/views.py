from django import http
from django.shortcuts import render, redirect, resolve_url
from cycling.cyclist.models import Cyclist


def cyclist_details(request, pk):
    current_cyclist = Cyclist.objects.get(pk=pk)
    all_cyclists = Cyclist.objects.order_by('first_name').all()
    context = {
        'title': 'The app for cyclists',
        'cyclists': all_cyclists,
        'current_cyclist': current_cyclist,
    }
    return render(request, 'cyclist_details.html', context)


def cyclists_all(request):
    all_cyclists = Cyclist.objects.order_by('first_name').all()
    result = ', '.join(f'{c.first_name} ({c.birthday})' for c in all_cyclists)
    # [first_name(id), first_name(id)]
    return http.HttpResponse(result)
