from django.urls import path
from . import views

urlpatterns=[
    path('create/', views.createCategory, name='Create-category'),
    path('lists/', views.categoryList, name='List-category'),
    path('list/',views.categoryById,name='single-category'),
    path('delete/',views.deleteCategory,name='delete-category')
]