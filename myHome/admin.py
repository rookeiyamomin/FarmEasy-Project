from django.contrib import admin
from .models import Cart,Sell_Product,worker_in_warehouse,worker_in_distribution,User_to_Farmeasy

admin.site.register(Cart)
admin.site.register(Sell_Product)
admin.site.register(worker_in_warehouse)
admin.site.register(worker_in_distribution)
admin.site.register(User_to_Farmeasy)

