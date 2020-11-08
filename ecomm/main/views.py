from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from main.forms import CreateUserForm

from main.decorators import unauth_user

from main.models import Order, Customer

from main.forms import OrderForm


@unauth_user
def signIn(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'signin.html', context)

@unauth_user
def signUp(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account created for " + username)
    context = {"form": form}
    return render(request, 'signup.html', context)


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    customersTotal = Customer.objects.count()
    ordersTotal = Order.objects.count()
    deliveredOrder = Order.objects.filter(status='Delivered').count()
    pendingOrder = Order.objects.filter(status='Pending').count()
    context = {
        "orders": orders,
        "customers": customers,
        "customerTotal": customersTotal,
        "ordersTotal": ordersTotal,
        "deliveredOrder": deliveredOrder,
        "pendingOrder": pendingOrder,
    }
    return render(request, 'home.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {"form": form}
    return render(request, 'update_order.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('home')
    context = {"order": order}
    return render(request, 'delete_order.html', context)


def signOut(request):
    logout(request)
    return redirect('signIn')




