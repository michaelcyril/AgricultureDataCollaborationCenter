from django.db import models
from AuthStakeholder.models import Wilaya, Mkoa, User


# Create your models here.
class Soi(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Soil(models.Model):
    name = models.ForeignKey(Soi, on_delete=models.CASCADE)
    wilaya_id = models.ForeignKey(Wilaya, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name.name


class SoilImage(models.Model):
    image = models.ImageField(upload_to="soil_images/", null=True, blank=True)
    soil_id = models.ForeignKey(Soil, on_delete=models.CASCADE)


class Prod(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.ForeignKey(Prod, on_delete=models.CASCADE)
    wilaya_id = models.ForeignKey(Wilaya, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to="product_images/", null=True, blank=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class Des(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Desease(models.Model):
    name = models.ForeignKey(Des, on_delete=models.CASCADE)
    wilaya_id = models.ForeignKey(Wilaya, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name.name


class DeseaseImage(models.Model):
    image = models.ImageField(upload_to="desease_images/", null=True, blank=True)
    desease_id = models.ForeignKey(Desease, on_delete=models.CASCADE)
