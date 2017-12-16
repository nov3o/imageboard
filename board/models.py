from django.db import models
from django.utils import timezone

class Post(models.Model):
	author = models.CharField(max_length=200)
	title = models.CharField(max_length=200)
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