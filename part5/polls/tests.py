from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question

# Create your tests here.
class QuestionModelTests(TestCase):
	def test_was_published_recently_with_future_question(self):
		"""
		was_published_recently() should return False for questions whose pub_date
		is in the future
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		"""
		Test the was_recently_published() method with a question with a pub date
		older than 1. Should return False
		"""
		# This is just outside the threshold for our method by 1 second and is therefore
		# not deemed as recent - should return False
		time = timezone.now() - datetime.timedelta(days=1, seconds=1)
		old_question = Question(pub_date=time)
		self.assertIs(old_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		"""
		Test the method with a question that falls within the specs of what
		is deemed 'recent' (within 1 day) - should return True
		"""
		# Just falls within our recent threshold by 1 second
		time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
		recent_question = Question(pub_date=time)
		self.assertIs(recent_question.was_published_recently(), True)

