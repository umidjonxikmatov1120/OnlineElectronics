from django.db import models

class DetailModel(models.Model):
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'detail'
        verbose_name_plural = 'details'


class CategoryModel(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ColorModel(models.Model):
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'


class SizeModel(models.Model):
    size = models.CharField(max_length=100)

    def __str__(self):
        return self.size

    class Meta:
        verbose_name = 'size'
        verbose_name_plural = 'sizes'


class ProductsModel(models.Model):
    image = models.ImageField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    new_price = models.FloatField()
    old_price = models.FloatField()
    discount = models.IntegerField()
    size = models.ForeignKey(SizeModel, on_delete=models.CASCADE)
    color = models.ForeignKey(ColorModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

