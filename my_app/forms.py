from django.forms import ModelForm
from .models import Order
from .models import Customer

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields ='__all__'
