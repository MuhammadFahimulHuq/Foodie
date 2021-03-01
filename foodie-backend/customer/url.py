from django.urls import path
from . import views

urlpatterns = [
    path('details/', views.customerLists, name="all-customer-lists"),

    path('detail/<str:pk>', views.customerList, name="customer-list"),

    path('registration/', views.createCustomer, name="customer-registration"),

    path('update/<str:pk>', views.updateCustomer, name="customer-update"),

    path('delete/<str:pk>', views.deleteCustomer, name="customer-delete")
]