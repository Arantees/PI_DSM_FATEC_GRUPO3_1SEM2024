from django.shortcuts import render, redirect, HttpResponseRedirect
from .services.repository.ProdutoRepository import ProductModel
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.urls import reverse
from Ferteliz import settings
from core.models import UserModel, ProductModel
from .forms import UserForm, ProductForm

# Create your views here.
def home (request):
    template_name = 'home.html'
    return render(request, template_name)

def cadastroMenu (request):
    return render(request, 'cadastroMenu.html')

def cadastroCliente(request):
    template_name = 'cadastroCliente.html'
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = UserForm()
        contexto = {'form': form}
        return render(request, template_name, contexto)

def login(request):
    template_name = 'login.html'
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, template_name, {'error': 'Invalid credentials'})
    return render(request, template_name)

def cadastroVendedor(request):
    template_name = 'cadastroVendedor.html'
    return render(request, template_name) 

def carrinho(request):
    template_name = 'carrinho.html'
    return render(request, template_name) 

def cadastroProdutos(request):
    template_name = 'cadastroProdutos.html'
    return render(request, template_name) 

def homeCliente(request):
    template_name = 'homeCliente.html'
    return render(request, template_name) 

def homeVendedor(request):
    template_name = 'homeVendedor.html'
    return render(request, template_name)

def profileVendedor(request):
    template_name = 'profileVendedor.html'
    return render(request, template_name)

def profileCliente(request):
    template_name = 'profileCliente.html'
    return render(request, template_name)

def list_products (request):
    products = ProductModel.objects.all()
    data = []
    for product in products:
        data.append({
            'name': product.name,
            'description': product.description,
            'price': str(product.price)
        })
    return JsonResponse(data, safe=False)
    #return render(request, 'list_products.html')

def add_product(request):
    template_name = 'add_product.html'
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'Produto cadastrado com sucesso!'})
        else:
            print(form.errors)  # Adicione esta linha para imprimir os erros do formulário no console
            errors = form.errors.as_json()
            return JsonResponse({'status': 'Formulário inválido', 'errors': errors}, status=400)
    else:
        form = ProductForm()
    return render(request, template_name, {'form': form})


