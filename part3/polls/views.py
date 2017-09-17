from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	output = ', '.join([q.question_text for q in latest_question_list])
	return HttpResponse("Hello World. You're at the polls index\n{0}".format(output))

def detail(request, question_id):
	return HttpResponse("You're looking at question {0}".format(question_id))

def results(request, question_id):
	response = "You're looking at the results of question {0}".format(question_id)
	return HttpResponse(response)

def vote(request, question_id):
	return HttpResponse("You're voting on question {0}".format(question_id))
