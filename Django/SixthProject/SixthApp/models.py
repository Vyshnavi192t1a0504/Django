from django.db import models

# Create your models here.
class CarData(models.Model):  #Model is class name , models is libraries or packages or python file

    car_name=models.CharField(max_length=150)
    """car_name is column name ,
    CharField is nothing but predefined class
    in sql we use varchar"""
    car_company=models.CharField(max_length=150)
    car_model=models.CharField(max_length=100)
    car_price=models.BigIntegerField()
    fuel_type=models.CharField(max_length=150)

