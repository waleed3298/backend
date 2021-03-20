from django.contrib import admin
from .models import Ad,Saved,Product,Order,OrderItem,Review,ShippingAddress,Blog,PriceIndex,YearlyIndices

admin.site.register(Ad)
admin.site.register(Saved)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
admin.site.register(ShippingAddress)
admin.site.register(Product)
admin.site.register(Blog)
admin.site.register(PriceIndex)
admin.site.register(YearlyIndices)