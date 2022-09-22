from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[path('', views.home, name="home"),
path('product/<str:name>', views.category, name="category_filter"),
path('cart', views.get_carts, name="cart"),
path('cart/<int:id>', views.add_to_cart, name="add_to_cart")] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)