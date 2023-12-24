from django.db import models


# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=100)
    course_duration=models.CharField(max_length=100)
    course_fees=models.IntegerField()

    def __str__(self):
        return self.course_name
class City(models.Model):
    city_name=models.CharField(max_length=100)

    def __str__(self):
        return self.city_name

class Student(models.Model):
    stud_name=models.CharField(max_length=150)
    stud_phno=models.BigIntegerField()
    stud_email=models.CharField(max_length=150)
    paid_fees=models.IntegerField()
    pending_fees=models.IntegerField()
    stud_course=models.ForeignKey(Course,on_delete=models.CASCADE) #id col will be linked here,CASCADE is used bcz in parent table
    # if we delete that related data shud be deleted in the child table also(dependent data in child table)
    stud_city=models.ForeignKey(City,on_delete=models.CASCADE)