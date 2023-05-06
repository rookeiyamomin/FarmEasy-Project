from django.shortcuts import render, redirect
from .models import Cart,Sell_Product,User_to_Farmeasy
from users.models import Profile
from .forms import CropForm,WarehouseWorkerForm,DistributionWorkerForm,UserToUsForm
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'myHome/index.html')

def cart_products(request):
    user_obj = Profile.objects.get(user=request.user)
    products = Cart.objects.filter(current_user=user_obj)
    total = 0
    for item in products:
        total += item.cart_obj.crop_price * item.cart_obj.crop_quan
    context = {'products':products,'total' :total}
    return  render(request,'myHome/cart.html',context)

@login_required(login_url="login")
def sell_product_view(request):

    crop_owner = Profile.objects.get(user=request.user)
    crop_name = request.POST.get("crop_name")
    crop_price = request.POST.get("crop_price")
    crop_quan = request.POST.get("crop_quan")
    crop_img = request.FILES.get("crop_img")
    
    # qr_img = request.FILES.get("crop_img")
    # list1 = []
    # for items in Sell_Product.objects.get(user=request.user):
    #     list1+=items
    
    if request.method == 'POST':
        product_obj = Sell_Product.objects.get_or_create(crop_owner=crop_owner,crop_name=crop_name,crop_quan=crop_quan,crop_price=crop_price,crop_img=crop_img)
        return redirect('home')

    # form = CropForm()
    # if request.method == 'POST':
    #     form = CropForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')
    
    # context = {'form' : form}
    context = {}
    return render(request,"myHome/sell_form.html",context)

@login_required(login_url="login")
def buy(request):
    user_obj = Profile.objects.get(user=request.user)
    crops = Sell_Product.objects.all()
    #crops = Sell_Product.objects.filter(crop_owner=user_obj)
    context = {'crops':crops} 
    return  render(request,'myHome/Buy.html',context)


def single_crop(request, pk):
    #user_obj = Profile.objects.get(user=request.user)
    crop = Sell_Product.objects.get(id=pk)
    context = {'crop':crop} 
    return  render(request,'myHome/product.html',context)
    
def add_to_cart(request):
    crop_obj = request.POST.get('crop_obj')

    login_user = Profile.objects.get(user=request.user)
    buy_obj = Sell_Product.objects.get(id=crop_obj)
    obj = Cart.objects.create(current_user=login_user, cart_obj=buy_obj)

    # product_obj = Cart.objects.create()
    # product_obj.current_user = Profile.objects.get(user=request.user)
    # product_obj.cart_obj = Sell_Product.objects.get(id=crop_obj)
    # product_obj.save()
    return render(request,'myHome/index.html')


@login_required(login_url="login")
def jobs(request):
    return render(request,'myHome/jobs.html')

def worker_in_warehouse_view(request):
    form = WarehouseWorkerForm()
    if request.method == 'POST':
        form = WarehouseWorkerForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = Profile.objects.get(user=request.user)
            instance.save()
            return redirect('home')
    context = {'form' : form}
    return render(request,"myHome/worker_in_warehouse_form.html",context)

def worker_in_distribution_view(request):
    form = DistributionWorkerForm()
    login_user = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = DistributionWorkerForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = Profile.objects.get(user=request.user)
            #instance.worker_img = request.FILES.get(request.POST)
            instance.save()
            return redirect('home')
    context = {'form' : form}
    return render(request,"myHome/worker_in_distribution_form.html",context)

def user_to_us_view(request):
    form = UserToUsForm()
    if request.method == 'POST':
        form = UserToUsForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            #instance.crop_owner = request.user
            #login_user = Profile.objects.get(user=request.user)
            instance.crop_owner = Profile.objects.get(user=request.user)
            instance.save()
            #form.save()
            return redirect('home')
    
    context = {'form' : form}
    return render(request,"myHome/user_to_us_form.html",context)

def check_status(request):
    user_obj = Profile.objects.get(user=request.user)
    crops = User_to_Farmeasy.objects.filter(crop_owner=user_obj)
    context = {'crops':crops}
    return render(request, 'myHome/status.html',context)

def about(request):
    context = {}
    return render(request, 'myhome/about.html')

def contact(request):
   return render(request, 'myhome/contact.html')  

def blog(request):
    return render(request, 'myhome/blog.html')    

def serve(request):
   return render(request, 'myhome/services.html') 

def sell(request):
   return render(request, 'myhome/sell.html')        
    
def cart(request):
    return render(request, 'myhome/cart.html') 

   