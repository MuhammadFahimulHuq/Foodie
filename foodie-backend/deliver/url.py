from django.urls import path
from . import views

urlpatterns = [
    path('details/', views.deliverLists, name="all-deliver-lists"),

    path('detail/<str:pk>', views.deliverList, name="deliver-list"),

    path('registration/', views.createDeliver, name="deliver-registration"),

    path('update/<str:pk>', views.updateDeliver, name="deliver-update"),

    path('delete/<str:pk>', views.deleteDeliver, name="deliver-delete")
]