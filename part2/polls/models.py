from django.db import models

# Create your models here.
class Question(models.Model):
	"""
	Variables used to represent database fields within the model
	"""
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

class Choice(models.Model):
	"""
	Variables used to represent database fields within the model
	"""
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
