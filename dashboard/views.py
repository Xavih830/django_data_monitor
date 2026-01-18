from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
import requests

# Create your views here.
@login_required
def index(request):
    response = requests.get(settings.API_URL)  # URL de la API
    posts = response.json()  # Convertir la respuesta a JSON

    # Número total de respuestas
    total_responses = len(posts)

    data = {
        'title': "Bienvenido al Dashboard",
        'total_responses': total_responses,
    }

    return render(request, 'dashboard/index.html', data)