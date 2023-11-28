from django.urls import path
from .views import index
from .views import list_data
from .views import remove_data
from .views import update_data

urlpatterns = [
    path('', index, name='index'),
    # Remove the line below
    # path('single_page/', single_page, name='single_page'),
    # Add other URL patterns as needed
    # your_app/urls.py
    path('list_data/', list_data, name='list_data'),
    path('remove_data/', remove_data, name='remove_data'),
    path('create_data/', remove_data, name='create_data'),
    path('update_data/', update_data, name='update_data'),
]