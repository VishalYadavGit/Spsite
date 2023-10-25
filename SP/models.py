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

# Create your models here.
