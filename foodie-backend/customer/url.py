from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('details', views.customerLists, name="all-customer-lists"),

    path('detail/<str:pk>', views.customerList, name="customer-list"),

    path('registration', views.createCustomer, name="customer-registration"),

    path('update/<str:pk>', views.updateCustomer, name="customer-update"),

    path('delete/<str:pk>', views.deleteCustomer, name="customer-delete"),

    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('hello/', views.helloWorld ,name="hello")
]