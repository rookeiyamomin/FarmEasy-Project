from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),
    
    path("about/", views.about, name="AboutUs"),
    path("contact", views.contact, name="ContactUs"),
    path("blog", views.blog, name="Blog"),
    path("service", views.serve, name="Services"),
    path("sell_product", views.sell_product_view, name="sell_product"),
    path("sell", views.sell, name="Sell"),
    path("buy", views.buy, name="buy"),
    path("products_url", views.cart_products, name="products_url"),
    path("cart", views.cart, name="Cart"),
    path("crop/<int:pk>", views.single_crop, name="crop"),
    path("add_to_cart", views.add_to_cart, name="add_to_cart"),
    path("jobs", views.jobs, name="jobs"),
    path("user_to_us", views.user_to_us_view, name="user_to_us"),
    path("check_status", views.check_status, name="check_status"),
    path("worker_in_warehouse_url", views.worker_in_warehouse_view, name="worker_in_warehouse_url"),
    path("worker_in_distribution_url", views.worker_in_distribution_view, name="worker_in_distribution_url"),
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)