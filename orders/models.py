from django.db import models
from customers.models import customer
from products.models import product

# Create your models here.
class Order(models.Model):

    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    STATUS_CHOICES=((ORDER_PROCESSED,"ORDER_PROCESSED"),
                    (ORDER_DELIVERED,"ORDER_DELIVERED"),
                    (ORDER_REJECTED,"ORDER_REJECTED"))
    
    order_status=models.IntegerField(choices=STATUS_CHOICES,default=CART_STAGE)
    total_price=models.FloatField(default=0)
    owner=models.ForeignKey(customer,on_delete=models.SET_NULL,null=True,related_name='orders')
    delete_status=models.IntegerField(choices=DELETE_CHOICES,default=LIVE)
    created_by=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "order-{}-{}".format(self.id,self.owner.name)

class orderedItem(models.Model):
    product=models.ForeignKey(product,related_name='added_carts',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='added_items')
