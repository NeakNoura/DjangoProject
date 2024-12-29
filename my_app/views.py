from django.shortcuts import render  , redirect
from .models import * 
from .forms import OrderForm,CustomerForm

def home(request):
    customer= Customer.objects.all()
    order = Order.objects.all()
    total_customer = customer.count()
    total_order = order.count()
    delivery = order.filter(status='Delivery').count()
    pending = order.filter(status="Pending").count()
    context = {'customer': customer,
               'order':order,
               'total_customer':total_customer,
               'total_order':total_order,
               'delivery':delivery,
               'pending':pending,}
    
    return render(request, 'my_app/dashboard.html', context)

def product(request):
    products = Product.objects.all()
    
    return render(request, 'my_app/product.html',{'products': products})

def customer(request, pk):
    customer=Customer.objects.get(id =pk)
    order = customer.order_set.all()
    order_count = order.count()
    context = {
        'customer':customer,
        'order_count':order_count,
    }
    return render(request, 'my_app/customer.html',context)


def dashboard(request):
    return render(request, 'my_app/dashboard.html')

def createOrder(request):
    form = OrderForm()
    if request.method == "POST":
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
       
    context = {
        'form': form,
    }
    return render(request, "my_app/ORDER.html", context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
            form = OrderForm(request.POST,instance=order)
            if form.is_valid():
                form.save()
                return redirect('/')
    context={
        'form':form
    }
    return render(request, 'my_app/ORDER.html',context)


def createCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to home or another page after creation
    return render(request, 'my_app/create_customer.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer
from .forms import CustomerForm

def updateCustomer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)  # Get the customer by pk
    form = CustomerForm(instance=customer)  # Create the form with the existing customer data

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()  # Save the updated customer data
            return redirect('customer', pk=customer.pk)  # Redirect to the customer detail page
        else:
            print(form.error)

    context = {
        'form': form,
        'customer': customer,
    }
    return render(request, 'my_app/update_customer.html', context)  # Render the update customer form
from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer

def deleteCustomer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    
    if request.method == "POST":
        customer.delete()  # Delete the customer object
        return redirect('home')  # Redirect to the home page or customer list

    context = {
        'customer': customer,
    }
from django.shortcuts import get_object_or_404, redirect
from .models import Order

def deleteOrder(request, pk):
    order = get_object_or_404(Order, pk=pk)
    print(f"Order to delete: {order}")  # Debugging line

    if request.method == "POST":
        order.delete()  # Delete the order
        print("Order deleted.")  # Debugging line
        return redirect('home')  # Redirect to home or any desired page

    # Render the confirmation page for GET requests
    return render(request, 'my_app/delete_order.html', {'order': order})
