from django.db import models

# Create your models here.
class InstrucVideo(models.Model):
	title = models.CharField(max_length =255)
	content = models.TextField(blank=True)
	video = models.CharField(max_length = 890)
	
