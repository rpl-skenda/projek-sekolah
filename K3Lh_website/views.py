from django.shortcuts import render
from K3Lh_website.models import Kotak

# Create your views here.
def login(request):
    return render(request, 'loginpage.html')

def home(request):
    return render(request, 'home.html')

def serbaserbi(request):
    return render(request, 'serbaserbi.html')

def pendataan(request):
    return render(request, 'pendataan.html')

def p3k(request):
    return render(request, 'p3k.html')

def hasil(request):
    box = Kotak.objects.all()

    konteks = {
        'box' : box
    }

    return render(request, 'hasil.html', konteks)

def profil(request):
    return render(request, 'profil.html')