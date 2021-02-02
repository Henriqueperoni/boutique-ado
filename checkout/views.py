from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IGJsAF5iYni04jpU12g6RIImeKl54EIi0Lbr80IqQF7knimOjpUyaeLY6jjy3qkb2cJ3VsYU2IB0MzcgVzwMUiK00AUhST193',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
