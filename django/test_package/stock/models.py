from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

from product.models import ProductModel
class StockModel(models.Model):
    quanlity = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)   
        ]
    )
    description = models.TextField()

    class Meta: 
        db_table = "stock"