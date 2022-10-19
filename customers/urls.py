from django.urls import path
from accounts import views as AccountViews
from . import views

urlpatterns = [
    path('', AccountViews.customer_dashboard, name='customer'),
    path('profile/', views.customer_profile, name='customer_profile'),
    path('my_orders/', views.my_orders, name='customer_my_orders'),
]