from django.db import models
from users.models import Profile
from django.contrib.auth.models import User
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw


    
class Sell_Product(models.Model):
    crop_owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
    crop_name = models.CharField(max_length=200,null=True,blank=True)
    crop_quan = models.IntegerField(blank=True, null=True)
    crop_price = models.IntegerField(blank=True, null=True)
    crop_img = models.ImageField(null=True,blank=True,default="wheat.jpg")
    #selling_qr_code = models.ImageField(upload_to='selling_qr_image',blank=True)
    
    def __str__(self):
        return str(self.crop_name)
    
    # def save(self, *args, **kwargs):
    #     qr_data = f"Seller:- {self.crop_owner}"
        
    #     qrcode_img = qrcode.make(qr_data)
    #     canvas = Image.new('RGB', (500, 500), 'white')
    #     canvas.paste(qrcode_img)
    #     fname = f'selling_qr_code-{self.crop_name}.png'
    #     buffer = BytesIO()
    #     canvas.save(buffer,'PNG')
    #     self.qr_code.save(fname, File(buffer), save=False)
    #     canvas.close()
    #     super().save(*args, **kwargs)

class Cart(models.Model):
    current_user = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
    cart_obj = models.ForeignKey(Sell_Product,null=True,blank=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return str(self.cart_obj)
 
class worker_in_warehouse(models.Model):
     user = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
     name = models.CharField(max_length=200,null=True,blank=True)
     phone = models.IntegerField(null=True,blank=True)
     email = models.EmailField(max_length=200,null=True,blank=True)
     location = models.CharField(max_length=200,null=True,blank=True)
     worker_img = models.ImageField(null=True,blank=True,upload_to="workers_img")

     def __str__(self):
        return str(self.name)
    
class worker_in_distribution(models.Model):
     user = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
     name = models.CharField(max_length=200,null=True,blank=True)
     phone = models.IntegerField(null=True,blank=True)
     email = models.EmailField(max_length=200,null=True,blank=True)
     location = models.CharField(max_length=200,null=True,blank=True)
     porter_img = models.ImageField(null=True,blank=True,upload_to="distributors_img")
     
     def __str__(self):
        return str(self.name)
    
    
# class Cart(models.Model):
#     cart_owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
#     cart_obj = models.CharField(max_length=200,null=True,blank=True)
    
#     def __str__(self):
#         return str(self.cart_owner)


class User_to_Farmeasy(models.Model):
    crop_owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
    crop_name = models.CharField(max_length=200,null=True,blank=True)
    crop_quantity = models.IntegerField(blank=True, null=True)
    crop_price = models.IntegerField(null=True,blank=True)
    crop_img = models.ImageField(null=True, blank=True)
    approved = models.BooleanField('Approved', default=False)

    def __str__(self):
        return str(self.crop_name)