from django.db import models
import os,sys

# Create your models here.
class Homesatu(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField(blank=True)
	photo =models.ImageField(upload_to='photo=/%Y/%m/%d')
	category_homesatu = models.ForeignKey('Category',on_delete=models.PROTECT,null=True)
    

class Insvid(models.Model):
	title = models.CharField(max_length =255)
	content = models.TextField(blank=True)
	video = models.FileField(upload_to='video=/%Y/%m/%d')
	podcast= models.ForeignKey('Homesatu',on_delete=models.CASCADE,null=True)


class Category(models.Model):
	name = models.CharField(max_length=255,db_index=True)
	
	
	
	def __str__(self):
		return self.name