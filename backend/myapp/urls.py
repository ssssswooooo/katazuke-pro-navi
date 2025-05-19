from django.urls import path

from . import views

urlpatterns = [
    path('items/', views.get_data, name='get_data'),
    path('items/create/', views.create_item, name='create_item'),
]