from django.db import models

class SaleOrder(models.Model):
    customer_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    region = models.CharField(max_length=50)  # India, USA, Europe

    def __str__(self):
        return f"{self.customer_name} - {self.region}"
