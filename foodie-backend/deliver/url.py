from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('details/', views.deliverLists, name="all-deliver-lists"),

    path('detail/<str:pk>', views.deliverList, name="deliver-list"),

    path('registration/', views.createDeliver, name="deliver-registration"),

    path('update/<str:pk>', views.updateDeliver, name="deliver-update"),

    path('delete/<str:pk>', views.deleteDeliver, name="deliver-delete")

    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token

    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]