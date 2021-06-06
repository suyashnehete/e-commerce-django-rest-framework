from django.urls import path

from products import views

urlpatterns = [
    path('', views.ProductView.as_view()),
    path('top/', views.TopProductView.as_view()),
    path('trending/', views.TrendingProductView.as_view()),
    path('<int:id>/', views.ProductRetrive.as_view()),
    path('images/<int:id>/', views.ProductImageView.as_view()),
    path('highlights/<int:id>/', views.ProductHighlightsView.as_view()),
    path('reviews/<int:id>/', views.ProductReviewView.as_view()),
    path('review/<int:id>/', views.ProductReviewRetrive.as_view()),
    path('wishlist/<int:id>/', views.WishlistView.as_view()),
    path('wishlist/', views.Wishlist.as_view()),
    path('tp/', views.tp.as_view()),
]