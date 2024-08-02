from django.db import models

# Create your models here.
class Bank(models.Model):
    ifsc = models.CharField(max_length=255, primary_key=True)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)

    # def __str__(self):
    #     return self.bank_name