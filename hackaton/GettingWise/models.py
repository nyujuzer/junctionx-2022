from django.db import models

# Create your models here.
class known_vendors(models.Model):
    #place, merchant name
    merchant_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    def __str__(self):
        return self.merchant_name


class item(models.Model):
    #receipt_id, date, cash_register, total, place, merchant name
    main_id = models.IntegerField()
    receipt_name = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    cash_register = models.CharField(max_length=100)
    total = models.FloatField()
    merchant_name = models.ForeignKey(known_vendors, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.main_id
    
