from django.db import models

class OrderModel(models.Model):
    product_id = models.PositiveIntegerField()
    class Meta:
        db_table="orders"