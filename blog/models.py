from django.db import models

# Create your models here.

class post(models.Model):
	title = models.CharField(max_length=300, default=' ')
	date = models.DateTimeField()
	text = models.TextField(default=' ')
	post_image = models.ImageField(upload_to='blog_images/')