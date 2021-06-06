from django.urls import path

from orders import views

urlpatterns = [
    path('', views.OrdersView.as_view()),
    path('<int:id>', views.OrderView.as_view()),
]