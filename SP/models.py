from django.db import models



class Machine_category(models.Model):
    Category_name=models.CharField(max_length=100)
    Category_img=models.ImageField(default=None)
    def __str__(self):
        return self.Category_name

class Machine(models.Model):
    category=models.ForeignKey(Machine_category,on_delete=models.CASCADE,related_name="machines")
    machine_name=models.CharField(max_length=100)
    machine_details=models.CharField(max_length=500)
    machine_img=models.ImageField()

    def __str__(self):
        return self.machine_name

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    phone=models.IntegerField()
    message=models.CharField(max_length=500)


# Create your models here.
