import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	"""
	Variables used to represent database fields within the model
	"""
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	def was_published_recently(self):
		now = timezone.now()
		#Would return true for future questions
		#return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
		#Fix by constraining pub_date on both ends
		return now - datetime.timedelta(days=1) <= self.pub_date <= now		

	def __str__(self):
		return self.question_text

class Choice(models.Model):
	"""
	Variables used to represent database fields within the model
	"""
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text
