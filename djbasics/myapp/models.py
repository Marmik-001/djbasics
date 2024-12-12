from django.db import models

# Create your models here.
class Student(models.Model):
    studentName = models.CharField("Name" , max_length=50 , blank=False)
    studentMobile = models.CharField('Mobile' , max_length=10  )
    studentEmail = models.CharField("Email", max_length=30, )
    studentPassword = models.CharField("Password",  max_length=50  )





    def __str__(self):
        return self.studentName