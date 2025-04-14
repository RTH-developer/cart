from django.shortcuts import render,redirect
from .models import Order,orderedItem
from products.models import product

# Create your views here.
def show_cart(request):
    user=request.user
    customer=user.customer_profile
    cart_obj, created=Order.objects.get_or_create(
           owner=customer,
           order_status=Order.CART_STAGE
         )
    context={'cart':cart_obj}

    return render(request,'cart.html',context)

def add_to_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        quantity = int(request.POST.get('quantity')) 
        product_id = request.POST.get('product_id')
        
        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        
        Product = product.objects.get(pk=product_id)
        ordered_item, created = orderedItem.objects.get_or_create(
            product=Product,
            owner=cart_obj,    
        )
        
        if created:
            ordered_item.quantity = quantity  # Set initial quantity
        else:
            ordered_item.quantity += quantity  # Increment existing quantity
            
        ordered_item.save()  # Save the model instance, not the quantity field
        return redirect('cart')