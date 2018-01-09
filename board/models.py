from django.db import models
from django.utils import timezone

class Thread(models.Model):
	author = models.CharField('Имя', max_length=70, blank=True)
	title = models.CharField(max_length=100, blank=True)
	text = models.TextField()
	published_date = models.DateTimeField()
	last_publish = models.DateTimeField() 
	count_number = models.IntegerField()

	def __str__(self):
		return self.title

class Post(models.Model):
	author = models.CharField('Имя', max_length=70, blank=True)
	text = models.TextField()
	published_date = models.DateTimeField()
	thread_number = models.IntegerField()
	count_number = models.IntegerField()

	def __str__(self):
		return self.text