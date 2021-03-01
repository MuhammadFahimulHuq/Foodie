from django.urls import path
from . import views

urlpatterns = [
    path('details/', views.restaurantLists, name="all-restaurant-lists"),

    path('detail/<str:pk>', views.restaurantList, name="restaurant-list"),

    path('registration/', views.createRestaurant, name="restaurant-registration"),

    path('update/<str:pk>', views.updateRestaurant, name="restaurant-update"),

    path('delete/<str:pk>', views.deleteRestaurant, name="restaurant-delete")
]