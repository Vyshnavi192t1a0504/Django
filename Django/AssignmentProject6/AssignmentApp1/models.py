from django.db import models

# Create your models here.
class MobileData(models.Model):  #Model is class name , models is libraries or packages or python file
    mobile_name=models.CharField(max_length=150)
    no_of_cameras=models.BigIntegerField()
    mobile_ram=models.CharField(max_length=100)
    mobile_price=models.BigIntegerField()
    mobile_color=models.CharField(max_length=150)