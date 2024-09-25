
from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('forgot/', views.forgot, name='forgot'),
    path('forgot_pass/', views.forgot_pass, name='forgot_pass'),
    path('firm_register/', views.firm_register, name='firm_register'),
]