from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    product_type = models.CharField(max_length=100)
    ean = models.CharField(max_length=13)  

    def __str__(self):
        return f"ID: {self.product_id}, Year: {self.year}, Type: {self.product_type}, EAN: {self.ean}"
