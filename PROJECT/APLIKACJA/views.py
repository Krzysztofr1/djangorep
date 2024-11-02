from django.shortcuts import render, HttpResponse
from .models import Pracownik, Sklep

# Create your views here.
def viewszhtml(request):
    wartosc_z_db = Pracownik.objects.all()
    return render(request,'index.html', context={"zmienna": wartosc_z_db})

def viewszid(request, id):
    wartosc_pojedyncza_z_db = Sklep.objects.get(id=id)
    return HttpResponse(f"{wartosc_pojedyncza_z_db.name} / {wartosc_pojedyncza_z_db.location}")