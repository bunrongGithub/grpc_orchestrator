import uuid
from django.db import models

class OrderModel(models.Model):
    STATUS_CHOICES = [
        ("PENDING","Pending"),
        ("COMPLATED","Completed"),
        ("FAILED","Failed"),
        ("COMPENSATED","Compansated")
    ]
    order_id=models.CharField(max_length=100,unique=True,default=uuid.uuid4,editable=False)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default="PENDING")
    created_at=models.DateTimeField(auto_now_add=True)
    items=models.JSONField(default=list)
    transaction_id=models.CharField(max_length=100,blank=True)
    def __str__(self):
        return f"Order {self.order_id}"
    class Meta:
        db_table="orders"