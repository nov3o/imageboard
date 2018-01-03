from django.db import models
from django.utils import timezone

"""
class Post(models.Model):
	author = models.CharField('Имя', max_length=70, blank=True)
	title = models.CharField(max_length=100, null=True)
	text = models.TextField()
	published_date = models.DateTimeField(
		blank=True, null=True)
	thrd = models.IntegerField(
		blank=True, null=True)

	def publish(self):
		self.thrd = self.id
		self.save(update_fields=['thrd'])
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
"""

class Thread(models.Model):
	author = models.CharField('Имя', max_length=70, blank=True) #maybe i should remove null
	title = models.CharField(max_length=100, blank=True, null=True) #maybe i should remove blank
	text = models.TextField()
	published_date = models.DateTimeField(
		blank=True, null=True) #maybe I should remove blank and null
	last_publish = models.DateTimeField(
		blank=True, null=True) #maybe I should add edit=True

	def __str__(self):
		return self.title

class Post(models.Model):
	author = models.CharField('Имя', max_length=70, blank=True)
	text = models.TextField()
	published_date = models.DateTimeField(
		blank=True, null=True) #maybe I should remove blank and null
	thread_id = models.IntegerField(
		blank=True, null=True) #maybe I should remove blank and null

	def __str__(self):
		return self.text