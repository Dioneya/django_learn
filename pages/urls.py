from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home_page_view, name='home')
]
