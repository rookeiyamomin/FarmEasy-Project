from django.db import models
from django.contrib.auth.models import User
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=500,null=True,blank=True)
    phone = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    pin = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    qr_code = models.ImageField(upload_to='qr_image',blank=True)
    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        qr_data = f"Name:- {self.name} \nPhone:- {self.phone}\nEmail:- {self.email}\nAddress:- {self.city},{self.pin},{self.state}"
        
        qrcode_img = qrcode.make(qr_data)
        canvas = Image.new('RGB', (500, 500), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.name}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
    
