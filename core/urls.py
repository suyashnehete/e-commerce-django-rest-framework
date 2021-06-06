from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from core import views

urlpatterns = [
    path('user/', views.UserView.as_view()),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('update/', views.UpdateView.as_view()),
    path('address/', views.AddressView.as_view()),
    #path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]