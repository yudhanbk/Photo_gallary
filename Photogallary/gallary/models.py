from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=300)
    descriptions = models.TextField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    