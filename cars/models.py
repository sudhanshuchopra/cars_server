from django.db import models

# Create your models here.
class Car(models.Model):
	Model=models.CharField(max_length=120)
	Price=models.CharField(max_length=120)
	image_url=models.TextField()
	#Desciption=models.TextField()
	Instance=models.CharField(max_length=120,default='')
	Colors=models.TextField(default='')
	Varients=models.TextField(default='')
	Engine=models.CharField(max_length=120,default='')
