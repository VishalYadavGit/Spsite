from django.db import models



class Machine_category(models.Model):
    Category_name=models.CharField(max_length=100)
    Category_img=models.ImageField(default=None)

    def __str__(self):
        return self.Category_name

class Brand(models.Model):
    brand_id=models.AutoField(primary_key=True)
    brand_name=models.CharField(max_length=100)
    brand_img = models.ImageField(upload_to="brands/", blank=True, null=True, default="motor.jpg")

    def __str__(self):
        return self.brand_name

class Machine(models.Model):
    category=models.ForeignKey(Machine_category,on_delete=models.CASCADE,related_name="machines")
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE,related_name="machines")
    machine_name=models.CharField(max_length=100)
    machine_descriptions=models.CharField(max_length=500)
    machine_details=models.JSONField()
    machine_img=models.ImageField()

    def __str__(self):
        return self.machine_name

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    phone=models.IntegerField()
    message=models.CharField(max_length=500)
    enquiry=models.CharField(max_length=100, default="General Enquiry")

    def __str__(self):
        return self.name + " - " + self.enquiry

class faq(models.Model):
    question=models.CharField(max_length=100)
    answer=models.CharField(max_length=500)

    def __str__(self):
        return self.question

class Carousel(models.Model):
    carousel_img=models.ImageField()
    carousel_title=models.CharField(max_length=100)

    def __str__(self):
        return self.carousel_title

# Create your models here.
