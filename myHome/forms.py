from django import forms 
from django.forms import ModelForm
from .models import Sell_Product,worker_in_warehouse,worker_in_distribution,User_to_Farmeasy

class CropForm(ModelForm):
    class Meta:
        model = Sell_Product
        #fields = '__all__'
        fields = ['crop_name','crop_quan','crop_price']
        
class WarehouseWorkerForm(ModelForm):
    class Meta:
        model = worker_in_warehouse
        #fields = '__all__'
        fields = ['name','phone','email','location','worker_img']

class DistributionWorkerForm(ModelForm):
    class Meta:
        model = worker_in_distribution
        #fields = '__all__'
        fields = ['name','phone','email','location','porter_img']
        

class UserToUsForm(ModelForm):
    class Meta:
        model = User_to_Farmeasy
        fields = ['crop_name','crop_quantity','crop_price','crop_img']
        
        
        