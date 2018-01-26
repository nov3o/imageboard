from django.db import models
from django.utils import timezone
import os.path

def content_file_name(instance, filename):
	ext = filename.split('.')[-1]
	total = len(Thread.objects.exclude(image='')) + len(Post.objects.exclude(image=''))
	#previos total was "len(Thread.objects.exclude(image='')) + len(Post.objects.exclude(image='')) - 1"
	filename = '%s.%s' % (str(total), ext)

	return os.path.join('media', filename)

class Thread(models.Model):
	image = models.ImageField('Пикча', upload_to=content_file_name)
	author = models.CharField('Имя', max_length=70, blank=True)
	title = models.CharField(max_length=100, blank=True)
	text = models.TextField()
	published_date = models.DateTimeField()
	last_publish = models.DateTimeField() 
	count_number = models.IntegerField()
	replies = models.CharField(blank=True, max_length=200)

	def __str__(self):
		return self.title

class Post(models.Model):
	image = models.ImageField(upload_to=content_file_name, blank=True)
	author = models.CharField('Имя', max_length=70, blank=True)
	text = models.TextField()
	published_date = models.DateTimeField()
	thread_number = models.IntegerField()
	count_number = models.IntegerField()
	replies = models.CharField(blank=True, null=True, max_length=200)

	def __str__(self):
		return self.text