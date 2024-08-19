from django.db import models

# Create your models here.
###
#Product
# Nom
#Prix
# lA quantite en stock
#Description
# Image
####
class Product(models.Model):
  name = models.CharField(max_length=128)
  slug = models.SlugField(max_length=128)
  price = models.FloatField(default=0.0)
  stock = models.IntegerField(default=0)
  description  = models.TextField(blank=True)
  thumbnail = models.ImageField(upload_to="products",blank=True,null=True)
  
  def __str__(self) -> str:
    return f"{self.name} ({self.stock})"
