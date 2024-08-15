from django.contrib import admin

from shop.models import DetailModel, CategoryModel, ColorModel, SizeModel, ProductsModel

admin.site.register(DetailModel)
admin.site.register(ProductsModel)
admin.site.register(CategoryModel)
admin.site.register(ColorModel)
admin.site.register(SizeModel)