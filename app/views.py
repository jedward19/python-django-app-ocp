import os
# from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render

from .models import PageView

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    hostname = hostname[:250]
    PageView.objects.create(hostname=hostname)

    return render(request, 'index.html', {
        'hostname': hostname,
        'count': PageView.objects.count()
    })


def health(request):
    state = {"status": "UP"}
    return JsonResponse(state)


def handler404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
