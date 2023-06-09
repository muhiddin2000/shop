from multiprocessing.spawn import import_main_path
from .views import home, product_with_category
from django.urls import path
from order.views import registerpage, loginpage, user_logout, orders, update

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:id>', product_with_category),
    path('register/', registerpage, name='register'),
    path('login/', loginpage, name='login'),
    path('logout/', user_logout, name='logout'),
    path('orders/', orders, name='orders'),
    path('update_item/', update)
]
