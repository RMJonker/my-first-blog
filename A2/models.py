from django.db import models
from django.utils import timezone

class Task(models.Model):
	owner = models.ForeignKey(
		'auth.User',
		default='0',
		on_delete=models.CASCADE,
		)
	taskname = models.CharField(max_length=200)
	text = models.TextField()
	due_date = models.DateField(
			default=timezone.now)
	important = models.BooleanField(
			default=False)

	def __str__(self):
		return self.taskname