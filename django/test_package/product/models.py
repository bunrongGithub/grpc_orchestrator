from django.db import models
class ProductModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200, null=True, blank=True)
    stock_id=models.PositiveBigIntegerField(null=True,blank=True)
    class Meta:
        db_table = "product"
