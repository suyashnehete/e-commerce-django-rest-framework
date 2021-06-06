from django.contrib import admin

from products.models import Product, ProductImage, ProductHighlights, ProductReviews

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductHighlights)
admin.site.register(ProductReviews)