from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=40, blank=False)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} - {self.description}'

class ProductComment(models.Model):
    user_name = models.CharField(max_length=40, blank=False)
    email = models.CharField(max_length=100, blank=False, default='SOME STRING')
    comment = models.CharField(max_length=600, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    checkbox = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user_name}: {self.comment}'