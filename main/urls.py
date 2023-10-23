from django.urls import path
from .views import *

urlpatterns = [
    path('index', index_view, name="index_url"),
    path('register/', register_ view, name="register_url"),
    path('', login_view, name="login_url"),
    path('blog-singe/<int:pk>/', name="singe_blog_url"),
    path('blog/', blog_view, name="blog_page_url"),
    path('service/', service_view, name="service_page_url"),
    path('menu/', menu_view, name="menu_page_url"),
    path('filter-meal-by-category/<int:pk>/',filter_meal_by_category, name='filter-meal-by-category_url')
]

