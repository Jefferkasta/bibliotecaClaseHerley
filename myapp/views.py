
from django.http import HttpResponse
from django.shortcuts import render
from .models import Libro 

# Create your views here.
#def index(request): #MELO
#  return HttpResponse("<h1>Welcome<h1>")

#def saludo(request,username):
 #   return HttpResponse("<h1>Hola %s<h1>" % username)

#def about(request): #MELO
#    return HttpResponse("<h2>About</h2>")

def home(request):
    return render(request,'home.html')

#CODIGO HERLEY
def index(request):
    return render(request,"templates/paginas/index.htm")

def editar(request):
    return render(request,'templates/paginas/editar.html')

def listar(request):
    libros = Libro.objets.all()
    
    return render(request, "libros/index.html", {'libros':libros})