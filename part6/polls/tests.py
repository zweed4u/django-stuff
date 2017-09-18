from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
from django.urls import reverse

# Create your tests here.

def create_question(question_text, days):
        """
        Create a question with the provided question_text and published with the number of days
        offset to now. (negative days for questions published in the past, positive for those
        questions that haven't been published yet)
        """
        time = timezone.now() + datetime.timedelta(days=days)
        return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
	def test_no_question(self):
		"""
		If no questions exist a message is displayed
		"""
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No polls are available")
		self.assertQuerysetEqual(response.context['latest_question_list'], [])

	def test_past_question(self):
		"""
		Questions with a pub_date in the past are displayed on the index page
		"""
		create_question(question_text="Past question.", days=-30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question.>'])

	def test_future_question(self):
		"""
		Questions witha a pub_date in the future aren't diaplyed on the index page
		"""
		create_question(question_text="Future question.", days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertContains(response, 'No polls are available')
		self.assertQuerysetEqual(response.context['latest_question_list'],[])

	def test_future_question_and_past_question(self):
		"""
		Even if both past and future questions exist only past questions are displayed
		"""
		create_question(question_text='Past question.', days=-30)
		create_question(question_text='Future question.', days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question.>'])

	def test_two_past_questions(self):
		"""
		The questions index page may display multiple questions
		"""
		create_question(question_text="Past question 1.", days=-30)
		create_question(question_text="Past question 2.", days=-5)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'], ['<Question: Past question 2.>','<Question: Past question 1.>'])

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

class QuestionDetailViewTests(TestCase):
	def test_future_question(self):
		"""
		The detail view of a question with a pub_date in the future should return a 404
		"""
		future_question = create_question(question_text='Future question.', days=5)
		url = reverse('polls:detail', args=(future_question.id,))
		response = self.client.get(url)
		self.assertEqual(response.status_code, 404)
	
	def test_past_question(self):
		"""
		The detail view of a question witha pub_date in the past displays the questions text
		"""
		past_question = create_question(question_text='Past question.', days=-5)
		url = reverse('polls:detail', args=(past_question.id,))
		response = self.client.get(url)
		self.assertContains(response, past_question.question_text)
