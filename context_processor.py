# cart/context_processor.py

from cart.cart import Cart

def cart_total_amount(request):
    cart = Cart(request)
    total_amount = sum([item['quantity'] * float(item['price']) for item in cart.session.get('cart', {}).values()])
    return {'cart_total_amount': total_amount}
